from videojuegos import *
DATOS = lee_datos('./data/Video_Game_Sales_as_of_Jan_2017.csv')

def test_lee_datos():
    print(DATOS)

#TEST 1#
def test_filtra_clasificcion_por_edades():
    print(filtra_clasificcion_por_edades(DATOS))

#TEST2#
def test_media_valoracion_por_juegos():
    print(calcula_media_valoracion_por_juego(DATOS, 'Call of Juarez: Bound in Blood'))

#TEST3#
def test_valor_maximo_ventas_juegos_por_anyo():
    print(valor_maximo_ventas_juegos_por_anyo(DATOS, 2016))




##############################################################################################################################
def test_valor_maximo_ventas_juegos_por_Plataforma():
    print(valor_maximo_ventas_juegos_por_Plataforma(DATOS, 'Wii'))
    print()



def test_maximo_ventas_por_plataforma():
    print(maximo_ventas_por_plataforma(DATOS))


def test_maximo_ventas_por_anyo_y_plataforma():
    print(maximo_ventas_por_anyo_y_plataforma(DATOS))
###############################################################################################################################



#TEST4#
def test_agrupa_por_genero(DATOS, accion):
    print(agrupa_por_genero(DATOS, accion))



def main():
  test_agrupa_por_genero(DATOS, 'Action')


if __name__ == '__main__':
    main()


