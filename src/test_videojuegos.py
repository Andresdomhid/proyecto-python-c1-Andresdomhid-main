from videojuegos import *
DATOS = lee_datos('./data/Video_Game_Sales_as_of_Jan_2017.csv')
#print(lee_datos('./data/Video_Game_Sales_as_of_Jan_2017.csv'))

#print(filtra_plataforma(Videojuego))

#calcula_media_valoracion_por_juego()

def test_media_valoracion_por_juegos():
    print(DATOS)

def main():
    test_media_valoracion_por_juegos()


if __name__ == '__main__':
    main()


