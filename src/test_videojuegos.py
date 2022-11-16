from videojuegos import *
DATOS = lee_datos('./data/Video_Game_Sales_as_of_Jan_2017.csv')

def test_lee_datos():
    print(DATOS)

def test_filtra_plataforma():
    print(filtra_plataforma(DATOS))

def test_media_valoracion_por_juegos():
    print(calcula_media_valoracion_por_juego(DATOS, 'Wii Sports'))

def main():
    test_media_valoracion_por_juegos()


if __name__ == '__main__':
    main()


