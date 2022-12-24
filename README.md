# ChessGMData
Grandmaster is the highest title awarded by FIDE to players who have surpassed an elo rating of 2500, and have achieved two norms in a tournament, demonstrating their exceptional talent of the game.

In this program I used the python library mysql.connector along with pandas to get relevant data from two datasets and answer the following questions:

- Which Federations have the most Grandmasters?
- How many Grandmasters achieved the title when they were 18 or younger?
- Around what year did most of the women GM's claim their title compared to men?
- What title year has the best players among the Grandmasters?
- How many GM's have surpassed Garry Kasparov in peak ELO rating?

## Data
Two Data files were used in this project, credit is given below.

### World's Chess GrandMasters Data
- Author: Rishabh Sethia
- https://www.kaggle.com/datasets/rishabh6377/worlds-chess-grandmasters-data

### GM Chess Games
- Author: Ronald Lázaro Cuevas
- https://www.kaggle.com/datasets/lazaro97/gm-chess-games (only players.csv was used)

## Results
Results from the SQL queries were all put into panda dataframes and printed to console, which are displayed below.


- Which Federations have the most Grandmasters?

![image](https://user-images.githubusercontent.com/66758884/209451982-213140a1-f7d7-47ca-b151-686164c840b7.png)

Russia ranks first, and the Soviet Union is high on the list as well before they became the Russian federation.

- How many Grandmasters achieved the title when they were 18 or younger?

![image](https://user-images.githubusercontent.com/66758884/209452029-851a82c1-0dd4-4016-91a9-55e71a554415.png)

There are 235 Grandmasters who achieved the title when they were 18 or younger, the youngest age being 13 years old.

- Around what year did most of the women GM's claim their title compared to men?

![image](https://user-images.githubusercontent.com/66758884/209452041-e4a56844-0765-4173-bcb8-016304135de5.png)

The first woman GM was Nona Gaprindashvili titled in 1978, although the sample size is small we can infer that women have been titled in more recent years compared to men.

- What title year has the best players among the Grandmasters?

![image](https://user-images.githubusercontent.com/66758884/209452056-ffe0be13-3b11-454e-a556-58338fe400b6.png)

Taking the average of might have skewed the results, as Gary Kasparov was the only titled GM in 1980 with the second highest max Elo rating of all time.

- How many GM's have surpassed Garry Kasparov in peak ELO rating?

![image](https://user-images.githubusercontent.com/66758884/209452060-cab421a0-f233-406f-977f-d6c64fc002cb.png)
