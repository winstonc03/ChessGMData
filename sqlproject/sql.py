import mysql.connector
from mysql.connector import Error
import datetime

create_gm_table = """
CREATE TABLE gm_data (
  name varchar(255),
  fide_id int,
  born date,
  birthplace varchar(255),
  died date,
  title_year year,
  federation varchar(255),
  sex char(1),
  notes varchar(255)
);
"""

create_player_table = """
CREATE TABLE player_data (
  name varchar(255),
  link varchar(255),
  last_game date,
  country varchar(255),
  max_elo int,
  current_elo int,
  total_games int
);
"""


def create_server_connection(host, user, password):
    connection = None
    try:
        connection = mysql.connector.connect(host=host, user=user, passwd=password)
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def populate_gm_table(connection, data):
    cursor = connection.cursor()
    cursor.execute("select database();")
    cursor.fetchone()
    cursor.execute('DROP TABLE IF EXISTS gm_data;')
    cursor.execute(create_gm_table)
    connection.commit()

    # loop through the data frame
    for i, row in data.iterrows():
        # here %S means string values
        sql = "INSERT INTO gm.gm_data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        try:
            cursor.execute(sql, tuple(row))
        except Error as err:
            # Some of the date inputs only include year
            # just add in an any month and day since we aren't using those values anyways
            tup = list(row)
            tup[2] = datetime.datetime(int(str(tup[2])[:4]), 1, 1)
            tup[4] = datetime.datetime(1111, 1, 1)
            cursor.execute(sql, tuple(tup))
        # the connection is not auto committed by default, so we must commit to save our changes
        connection.commit()

def populate_player_table(connection, data):
    cursor = connection.cursor()
    cursor.execute("select database();")
    cursor.fetchone()
    cursor.execute('DROP TABLE IF EXISTS player_data;')
    cursor.execute(create_player_table)
    connection.commit()

    # loop through the data frame
    for i, row in data.iterrows():
        # here %S means string values
        sql = "INSERT INTO gm.player_data VALUES (%s,%s,%s,%s,%s,%s,%s)"
        try:
            cursor.execute(sql, tuple(row))
        except Error as err:
            # Some of the date inputs only include year
            # just add in an any month and day since we aren't using those values anyways
            tup = list(row)
            tup[2] = datetime.datetime(int(str(tup[2])[:4]), 1, 1)
            cursor.execute(sql, tuple(tup))
        # the connection is not auto committed by default, so we must commit to save our changes
        connection.commit()

def results_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result
