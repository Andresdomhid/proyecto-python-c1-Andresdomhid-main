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
def filtra_clasificcion_por_edades(Videojuegos):
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
def valor_maximo_ventas_juegos_por_anyo(videojuegos, anyo):
    result = []
    for videojuego in videojuegos:
        if videojuego.Year_of_Release == anyo:
            calculado = (videojuego.Year_of_Release, videojuego.Name, videojuego.Platform, videojuego.Global_Sales)
            result.append(calculado)
            result = sorted(result, reverse = True, key = lambda x:x[3])
    return result[0]



def valor_maximo_ventas_juegos_por_Plataforma(videojuegos, plataforma):
    result = defaultdict(float)
    for videojuego in videojuegos:
        if videojuego.Platform == plataforma:
            if result[(videojuego.Name,videojuego.Platform)]<videojuego.Global_Sales:
                result[(videojuego.Name, videojuego.Platform)]= videojuego.Global_Sales
            else:
                result[(videojuego.Name, videojuego.Platform)]=result[(videojuego.Name, videojuego.Platform)]
    return result


def maximo_ventas_por_plataforma(videojuegos):
    
    lista_plataforma_venta = [(videojuego.Year_of_Release, videojuego.Platform) for videojuego in videojuegos]
    lista_ordenada = sorted(lista_plataforma_venta, key= lambda x:x[1])
    return dict(lista_ordenada)



def maximo_ventas_por_anyo_y_plataforma(videojuegos):
    result = []
    for videojuego in videojuegos:
        calculado = (videojuego.Platform, videojuego.Name, videojuego.Year_of_Release, videojuego.Global_Sales)
        result.append(calculado)
        result = sorted(result, reverse=True, key= lambda x:x[2])
    return result





#CUARTA FUNCION
def agrupar_videojuegos_por_anyo(videojuegos, year):
    res = dict()
    for videojuego in videojuegos:
        if videojuego.Year_of_Release == year:
            clave = videojuego.Year_of_Release()
            if clave not in res:
                res[clave] = [videojuego]
            else:
                res[clave].append(videojuego.Name)
    return res



def agrupar_juegos_por_genero(videojuegos, genero):
    result = defaultdict(list)
    for videojuego in videojuegos:
        if Videojuego.Genre == genero:
            result[videojuego.Genre].append(videojuego.Name)
    return result















def valor_maximo_ventas_juegos_por_Plataforma(videojuegos, plataforma):
    result = defaultdict(float)
    for videojuego in videojuegos:
        if videojuego.Platform == plataforma:
            if result[(videojuego.Name,videojuego.Platform)]<videojuego.Global_Sales:
                result[(videojuego.Name, videojuego.Platform)]= videojuego.Global_Sales
            else:
                result[(videojuego.Name, videojuego.Platform)]=result[(videojuego.Name, videojuego.Platform)]
    return result


def maximo_ventas_por_plataforma(videojuegos):
    
    lista_plataforma_venta = [(videojuego.Year_of_Release, videojuego.Platform) for videojuego in videojuegos]
    lista_ordenada = sorted(lista_plataforma_venta, key= lambda x:x[1])
    return dict(lista_ordenada)



def maximo_ventas_por_anyo_y_plataforma(videojuegos):
    result = []
    for videojuego in videojuegos:
        calculado = (videojuego.Platform, videojuego.Name, videojuego.Year_of_Release, videojuego.Global_Sales)
        result.append(calculado)
        result = sorted(result, reverse=True, key= lambda x:x[2])
    return result