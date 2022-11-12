from collections import namedtuple
import csv
from datetime import datetime


Videojuego = namedtuple('Videojuegos', 'Name,Platform,Year_of_Release,Genre,Publisher,NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales,Critic_Score,Critic_Count,User_Score,User_Count,Rating')
def lee_datos(Nombre_fichero):
    result = []
    with open(Nombre_fichero) as v:
        Lector = csv.reader(v)
        next(Lector)
        for Listado in Lector:
            Name = str(Listado[0])
            Platform = str(Listado[1])
            Year_of_Release = Listado[2]
            Genre = str(Listado[3])
            Publisher = str(Listado[4])
            NA_Sales = float(Listado[5])
            EU_Sales = float(Listado[6])
            JP_Sales = float(Listado[7])
            Other_Sales = float(Listado[8])
            Global_Sales = float(Listado[9])
            Critic_Score = str(Listado[10])
            Critic_Count = str(Listado[11])
            User_Score = str(Listado[12])
            User_Count = str(Listado[13])
            Rating = bool(Listado[14])
            tupla = Videojuego(Name,Platform,Year_of_Release,Genre,Publisher,NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales,Critic_Score,Critic_Count,User_Score,User_Count,Rating)
            result.append(tupla)
    return result