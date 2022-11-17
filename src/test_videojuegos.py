from videojuegos import *
DATOS = lee_datos('./data/Video_Game_Sales_as_of_Jan_2017.csv')

def test_lee_datos():
    print(DATOS)

def test_filtra_plataforma():
    print(filtra_plataforma(DATOS))

def test_media_valoracion_por_juegos():
    print(calcula_media_valoracion_por_juego(DATOS, 'Wii Sports'))

def test_agrupa_videojuegos_por_anyo():
    print(agrupar_videojuegos_por_anyo(DATOS))

def test_valor_maximo_ventas_juegos_por_Plataforma():
    print(valor_maximo_ventas_juegos_por_Plataforma(DATOS))
    print()

def main():
   test_valor_maximo_ventas_juegos_por_Plataforma()


if __name__ == '__main__':
    main()


