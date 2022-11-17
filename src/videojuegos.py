import csv
from collections import namedtuple,defaultdict

Videojuego = namedtuple('Videojuegos', 'Name,Platform,Year_of_Release,Genre,Publisher,NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales,Critic_Score,Critic_Count,User_Score,User_Count,Rating')



def lee_datos(Nombre_fichero):
    result = []
    with open(Nombre_fichero, encoding= "utf-8") as v:
        Lector = csv.reader(v, delimiter=";")
        next(Lector)
        for Listado in Lector:
            Name = Listado[0]
            Platform = str(Listado[1])
            if Listado[2]== '':
                Year_of_Release=0
            else:
                Year_of_Release = int(Listado[2])
            Genre = str(Listado[3])
            Publisher = str(Listado[4])
            if Listado[5]== '':
                NA_Sales=0.0
            else:
                NA_Sales= float(Listado[5])
            if Listado[6]== '':
                EU_Sales=0.0
            else:
                EU_Sales = float(Listado[6])
            if Listado[7]== '':
                JP_Sales=0.0
            else:
                JP_Sales = float(Listado[7])
            if Listado[8]== '':
                Other_Sales=0.0
            else:
                Other_Sales = float(Listado[8])
            if Listado[9]== '':
                Global_Sales=0.0
            else:
                Global_Sales = float(Listado[9])
            if Listado[10]== '':
                Critic_Score=0.0
            else:
                Critic_Score = float(Listado[10])
            if Listado[11]== '':
                Critic_Count=0
            else:
                Critic_Count = int(Listado[11])
            if Listado[12]== '':
                User_Score=0.0
            else:
                User_Score =float(Listado[12])
            if Listado[13]== '':
                User_Count=0
            else:
                User_Count = int(Listado[13])
            if Listado[14]== '':
                Rating=None
            else:
                Rating = bool(Listado[14]=='E')
            
            tupla = Videojuego(Name,Platform,Year_of_Release,Genre,Publisher,NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales,Critic_Score,Critic_Count,User_Score,User_Count,Rating)
            result.append(tupla)
    return result




#PRIMERA FUNCION
def filtra_plataforma(Videojuegos):
    result = []
    for Videojuego in Videojuegos:
        if Videojuego.Rating == True:
            muestra = (Videojuego.Name)
            result.append(muestra)
    return 'Los juegos para todas las edades son:', result



#SEGUNDA FUNCION
def calcula_media_valoracion_por_juego(videojuegos, name):
    result = []
    for videojuego in videojuegos:
        if videojuego.Name == name:
            result.append(videojuego.Critic_Score)
            result.append(videojuego.User_Score)
    return sum(result)//len(result)

### CALCULA LA VALORACION MEDIA ENTRE LOS USUARIOS Y LOS CRITICOS DEL JUEGO SELECCIONADO ###




#TERCERA FUNCION
def valor_maximo_ventas_juegos_por_Plataforma(videojuegos):
    result = defaultdict(float)
    for videojuego in videojuegos:
        if result[(videojuego.Name,videojuego.Platform)]<videojuego.Global_Sales:
            result[(videojuego.Name, videojuego.Platform)]= videojuego.Global_Sales
    return result

#CUARTA FUNCION
def agrupar_videojuegos_por_anyo(videojuegos):
    res = dict()
    for videojuego in videojuegos:
        clave = videojuego.Year_of_Release()
        if clave not in res:
            res[clave] = [videojuego]
        else:
            res[clave].append(videojuego)
    return res

