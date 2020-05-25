def count_games(file_name):
    f = open(file_name, "r")
    n=0
    for _ in f:
        n=n+1
    f.close()
    return n


# zamknięcie pliku
def decide(file_name, year):
    game_list = open(file_name, "r")
    for game in game_list:
        if str(year) in game:
            return True
    raise ValueError


def get_latest(file_name):
    cat_list=get_category(file_name, 2)
    #poprawic czytelnośc przez przypisanie 0, 1:
    game_name=cat_list[1][cat_list[0].index(max(cat_list[0]))][0]
    return(game_name)





#zamknięcie pliku/ with open file
def tekst_to_list(file_name):
    game_list = open(file_name, "r")
    good_list=[]
    for game in game_list:
        good_list=good_list+[game.split("\t")]
    return good_list


def count_by_genre(file_name, genre):
    genre_list=get_category(file_name, 3)[0]
    n=0
    for game in genre_list:
        if game==genre:
            n=n+1
    return n



def get_line_number_by_title(file_name, title):
    title_list=get_category(file_name, 0)[0]
    if title in title_list:
        return title_list.index(title)+1
    else: 
        raise ValueError


def sort_abc(file_name):
    title_list=get_category(file_name, 0)[0]
    if title_list == []:
        raise ValueError
    n=0 
    sorted_list=sort_alpha(title_list)
    return sorted_list




def sort_alpha(title_list):
    loops=len(title_list)
    while loops>0
        for n in range(0, len(title_list)-1):
            if title_list[n]>title_list[n+1]:
                current_title=title_list[n]
                title_list[n]=title_list[n+1]
                title_list[n+1]=current_title
        loops=loops-1
    return title_list

#struktura: set 
def get_genres(file_name):
    genere_list=get_category(file_name, 3)[0]
    single_genere=[]
    for genere in genere_list:
        if genere not in single_genere:
            single_genere.append(genere)
    sorted_genere=sort_alpha(single_genere)
    return sorted_genere


def when_was_top_sold_fps(file_name):
    genere_list=get_category(file_name, 3)[0]
    sales_stats=get_category(file_name, 1)[0]
    production_dates=get_category(file_name, 2)[0]
    FPS_sales=[]
    for n in range(0, len(genere_list)):
        if genere_list[n] == "First-person shooter":
            FPS_sales.append(float(sales_stats[n]))
    if FPS_sales != []:
        return int(production_dates[sales_stats.index(str(max(FPS_sales)))])
    else:
        raise ValueError


file_name="game_stat.txt"
