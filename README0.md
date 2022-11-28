# proyecto-python-c1-Andresdomhid-main
Andrés Domínguez Hidalgo

Este conjunto de datos contiene una lista de videojuegos con ventas superiores a 100.000 copias junto con valoraciones de críticos y usuarios. Es un raspado web combinado de VGChartz y Metacritic junto con valores de año de lanzamiento ingresados manualmente para la mayoría de los juegos con un año de lanzamiento faltante. La codificación original fue creada por Rush Kirubi y se puede encontrar aquí, pero limitó los datos para incluir solo un subconjunto de plataformas de videojuegos. No todos los videojuegos enumerados tienen información sobre Metacritic, por lo que el conjunto de datos tiene valores faltantes.

Contenido

Los campos incluyen:

Nombre - El nombre del juego

Plataforma - Plataforma del lanzamiento de los juegos

Añodelanzamiento - Año de lanzamiento del juego

Género - Género del juego

Editor - Editor del juego

NA_Sales - Ventas en América del Norte (en millones)

EU_Sales - Ventas en Europa (en millones)

JP_Sales - Ventas en Japón (en millones)

Other_Sales - Ventas en el resto del mundo (en millones)

Global_Sales - Ventas mundiales totales (en millones)

Critic_score - Puntuación agregada compilada por el personal de Metacritic

Critic_count - El número de críticos utilizados para llegar a la puntuación de la crítica

User_score - Puntuación de los suscriptores de Metacritic

User_count - Número de usuarios que dieron la puntuación de usuario

Calificación - Las calificaciones de esRB




# FUNCIONES: SEGUNDA ENTREGA
## Primera Función
`def filtra_clasificcion_por_edades(Videojuegos):`
 La función devuelve una lista con todos los juegos con una clasificación 'everyone', es decir, apto para todos los públicos.

## Segunda Función
`def calcula_media_valoracion_por_juego(videojuegos, name):`
La función devuelve una lista con la valoración media entre la crítica y los usuarios según el juego seleccionado.

## Tercera Función
`def valor_maximo_ventas_juegos_por_anyo(videojuegos, anyo):`: 
La función devuelve una lista con el juego más vendido del año seleccionado.

## Cuarta Función
`def agrupa_por_genero(videojuegos, genero):`: 
La función devuelve un diccionario con los juegos que pertenecen al género seleccionado.