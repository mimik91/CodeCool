# Printing functions
print("What is the name of data file?")
datafile=input()
print("How many games are in the file?")
from reports import count_games
print(count_games(datafile))
year=input("Is there a game from a given year?")
from reports import decide
print(decide(datafile, year))
print("Which is the latest game?")
from reports import get_latest
print(get_latest(datafile))
genre=input("How many games are in the file by genre?")
from reports import count_by_genre
print(count_by_genre(datafile, genre))
title=input("What is the line number of a given title?")
from reports import get_line_number_by_title
print(get_line_number_by_title(datafile, title))
print("Can you give me the alphabetically ordered list of the titles?")
from reports import sort_abc
print(sort_abc(datafile))
print("Which genres occur in the data file?")
from reports import get_genres
print(get_genres(datafile))
print("What is the release year of the top sold first-person shooter game?")
from reports import when_was_top_sold_fps
print(when_was_top_sold_fps(datafile))
