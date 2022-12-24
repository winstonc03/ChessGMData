# main.py
import sql as db
import pandas as pd

def main():
    # Hidden password, If you want to test it then input your own :)
    pw = "foo"

    gm_data = pd.read_csv('data/WorldChessGrandMaster.csv', index_col=False, delimiter=',')
    player_data = pd.read_csv('data/players.csv', index_col=False, delimiter=',')
    connection = db.create_server_connection("localhost", "root", pw)
    create_GM_database_query = "CREATE DATABASE gm"
    db.create_database(connection, create_GM_database_query)

    connection = db.create_db_connection("localhost", "root", pw, "gm")
    db.populate_gm_table(connection, gm_data)
    db.populate_player_table(connection, player_data)

    fed_query = """
    SELECT federation, COUNT(*) FROM gm_data
    GROUP BY federation
    ORDER BY COUNT(*) DESC
    LIMIT 10;
    """
    federation_results = db.results_query(connection, fed_query)
    pd_visualizer(federation_results, ["federation", "number_players"])

    young_gm_query = """
    SELECT name, born, title_year FROM gm_data
    WHERE title_year - YEAR(born) <= 18
    ORDER BY title_year - YEAR(born) ASC;
    """
    young_gm_results = db.results_query(connection, young_gm_query)
    pd_visualizer(young_gm_results, ["name", "birthdate", "title_year"])

    gender_gm_query = """
    SELECT sex, COUNT(*), ROUND(AVG(title_year)) FROM gm_data
    GROUP BY sex
    ORDER BY COUNT(*) DESC; 
    """
    gender_gm_results = db.results_query(connection, gender_gm_query)
    pd_visualizer(gender_gm_results, ["gender", "number_players", "title year average"])

    title_year_query = """
    SELECT title_year, ROUND(AVG(max_elo)) FROM gm_data
    INNER JOIN player_data ON gm_data.name = player_data.name
    GROUP BY title_year
    ORDER BY ROUND(AVG(max_elo)) DESC
    LIMIT 10;
    """
    title_year_results = db.results_query(connection, title_year_query)
    pd_visualizer(title_year_results, ["title_year", "max_elo_average"])

    # Using a subquery
    kasparov_query = """
    SELECT name, country, max_elo FROM player_data
    WHERE max_elo >= (
        SELECT max_elo FROM player_data
        WHERE name = "Kasparov, Garry")
    """
    kasparov_results = db.results_query(connection, kasparov_query)
    pd_visualizer(kasparov_results, ["name", "country", "max_elo"])


def pd_visualizer(results, columns):
    from_db = []
    for result in results:
        result = list(result)
        from_db.append(result)

    df = pd.DataFrame(from_db, columns=columns)
    print(df)


if __name__ == "__main__":
    main()
