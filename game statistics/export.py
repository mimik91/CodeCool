# Export functions
import sys
from reports import count_games, decide, get_latest ,count_by_genre,  get_line_number_by_title, sort_abc, get_genres, when_was_top_sold_fps

source_file=sys.argv[1]
export_file=sys.argv[2]
year=sys.argv[3]
genere=sys.argv[4]
game_title=sys.argv[5]
print(source_file, export_file, year, genere, game_title)


#try exept <- na wypadek gdyby plik był używany przez inny program
f = open(export_file, "a")
f.write(str(count_games(source_file)))
f.write(str(decide(source_file, year)))
f.write(get_latest(source_file))
f.write(str(count_by_genre(source_file, genere)))
f.write(str(get_line_number_by_title(source_file, game_title)))
f.write((";").join(sort_abc(source_file)))
f.write((";").join(get_genres(source_file)))
f.write(str(when_was_top_sold_fps(source_file)))
f.close()