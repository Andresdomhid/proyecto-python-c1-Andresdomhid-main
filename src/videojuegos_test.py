from collections import namedtuple
from platform import platform



juego = namedtuple('juego', 
'rank', 'name', 'platmform', 'year', 'genre', 'plublisher', 'NA_sales', 'EU_sales', 'JP_sales', 'other_sales', 'global_sales', 'critic_score', 'critic_count', 'user_score', 'user_count', 'rating')

def lee_juegos(fichero):
    videojuegos = []
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next (lector)
        for rank,name, platform, year, genre, publisher, NA_sales, EU_sales, JP_sales, other_sales, global_sales, critic_score, critic_count, user_score, user_count, rating in lector:
            year = int(year)
            NA_sales = float(NA_sales)
            EU_sales = float(EU_sales)
            JP_sales = float(JP_sales)
            other_sales = float(other_sales)
            global_sales = float(global_sales)
            critic_score = float(critic_score)
            critic_count = float(critic_count)
            user_score = float(user_score)
            user_count = float(user_count)
            videojuegos.append(juego(rank,name, platform, year, genre, publisher, NA_sales, EU_sales, JP_sales, other_sales, global_sales, critic_score, critic_count, user_score, user_count, rating))
    return videojuegos
