from videojuegos import *
DATOS = lee_datos('./data/Video_Game_Sales_as_of_Jan_2017.csv')

def test_lee_datos():
    print(DATOS)

def test_filtra_clasificcion_por_edades():
    print(filtra_clasificcion_por_edades(DATOS))

def test_media_valoracion_por_juegos():
    print(calcula_media_valoracion_por_juego(DATOS, 'NBA 2K17'))

def test_agrupa_videojuegos_por_anyo():
    print(agrupar_videojuegos_por_anyo(DATOS))

def test_valor_maximo_ventas_juegos_por_Plataforma():
    print(valor_maximo_ventas_juegos_por_Plataforma(DATOS, 'Wii'))
    print()

def test_agrupar_videojuegos_por_anyo():
    print(agrupar_videojuegos_por_anyo(DATOS, 'Dino Crisis'))




def test_maximo_ventas_por_plataforma():
    print(maximo_ventas_por_plataforma(DATOS))


def test_maximo_ventas_por_anyo_y_plataforma():
    print(maximo_ventas_por_anyo_y_plataforma(DATOS))

def main():
   test_valor_maximo_ventas_juegos_por_Plataforma()


if __name__ == '__main__':
    main()


