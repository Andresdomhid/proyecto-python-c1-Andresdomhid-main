import csv
from collections import namedtuple as nt



videojuegos = nt('juego', 'Name, Platform, Year, Genre, Publisher, NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales, Critic_Score, Critic_Count, User_Score, User_Count, Rating')


def lee_juegos(fichero = './data/Video_Game_Sales_as_of_Jan_2017.csv'):
    videojuegos = []
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next (lector)
        for Name, Platform, Year, Genre, Publisher, NA_Sales, EU_Sales, JP_Sales, other_Sales, global_Sales, Critic_Score, Critic_Count, User_Score, User_Count, Rating in lector:
            Name = str(Name)
            Platform = str(Platform)
            Year = int(Year)
            Genre = str(Genre)
            Publisher = str(Publisher)
            NA_Sales = float(NA_Sales)
            EU_Sales = float(EU_Sales)
            JP_Sales = float(JP_Sales)
            Other_Sales = float(Other_Sales)
            Global_Sales = float(Global_Sales)
            Critic_Score = float(Critic_Score)
            Critic_Count = float(Critic_Count)
            User_Score = float(User_Score)
            User_Count = float(User_Count)
            Rating = bool(Rating)
            videojuegos.append(videojuegos(Name, Platform, Year, Genre, Publisher, NA_Sales, EU_Sales, JP_Sales, other_Sales, global_Sales, Critic_Score, Critic_Count, User_Score, User_Count, Rating))
    return videojuegos