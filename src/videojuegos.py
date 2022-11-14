import csv
from collections import namedtuple

videojuego = namedtuple('videojuegos', 'Name,Platform,Year_of_Release,Genre,Publisher,NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales,Critic_Score,Critic_Count,User_Score,User_Count,Rating')

with open('./data/Video_Game_Sales_as_of_Jan_2017.csv', encoding= 'utf-8') as f:
    lector = csv.reader(f)
    next(lector)
    videojuegos = []
    for Name,Platform,Year_of_Release,Genre,Publisher,NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales,Critic_Score,Critic_Count,User_Score,User_Count,Rating in lector:
        Name = str(Name)
        Platform = str(Platform)
        Year_of_Release = (Year_of_Release)
        Genre = str(Genre)
        Publisher = str(Publisher)
        NA_Sales = float(NA_Sales)
        EU_Sales = float(EU_Sales)
        JP_Sales = float(JP_Sales)
        Other_Sales = float(Other_Sales)
        Global_Sales = float(Global_Sales)
        Critic_Score = str(Critic_Score)
        Critic_Count = str(Critic_Count)
        User_Score = str(User_Score)
        User_Count = str(User_Count)
        Rating = bool(Rating)
        videojuegos.append(videojuego(Name, Platform, Year_of_Release, Genre, Publisher, NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales, Critic_Score, Critic_Count, User_Score, User_Count, Rating))
   

def lee_ficheros(videojuegos):
    print(videojuegos)



def calcula_plataformas(videojuegos):
    






#def filtra_por_plataforma(videojuegos, Platform):
    #filtradas = [(p, s) for p, s in videojuegos if p in Platform]
    #return filtradas
