from collections import namedtuple
from videojuegos import *

#lee_ficheros(videojuegos)

Juegos_Wii = filtra_por_plataforma(videojuegos, 'Wii')
print(Juegos_Wii)