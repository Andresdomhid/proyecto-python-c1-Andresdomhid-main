# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  \<XX\>/\<YY\>)
Autor/a: \<Andrés Domínguez Hidalgo\>   uvus:\<FNJ0910\>

Aquí debes añadir la descripción del dataset y un enunciado del dominio del proyecto.


## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **\<videojuegos.py\>**: Describe aquí el módulo principal.
  * **\<test_videojuegos.py\>**: Describe aquí el módulo de pruebas.
  * **\<modulo2.py\>**: Añade descripciones para el resto de módulos que pueda tener tu proyecto. Por ejemplo, sería conveniente tener un módulo separado con funciones genéricas para dibujar gráficas y/o otro con funciones genéricas de conversión de tipos. 
* **/data**: Contiene el dataset o datasets del proyecto
    * **\<Video_Game_Sales_as_of_Jan_2017.csv\>**: Este conjunto de datos contiene una lista de videojuegos con ventas superiores a 100.000 copias junto con valoraciones de críticos y usuarios. Es un raspado web combinado de VGChartz y Metacritic junto con valores de año de lanzamiento ingresados manualmente para la mayoría de los juegos con un año de lanzamiento faltante. La codificación original fue creada por Rush Kirubi y se puede encontrar aquí, pero limitó los datos para incluir solo un subconjunto de plataformas de videojuegos. No todos los videojuegos enumerados tienen información sobre Metacritic, por lo que el conjunto de datos tiene valores faltantes.

    
## Estructura del *dataset*

Aquí debes describir la estructura del dataset explicando qué representan los datos que contiene y la descripción de cada una de las columnas.

El dataset está compuesto por \<15\> columnas, con la siguiente descripción:

* **\<nombre>**: de tipo \<str\>, representa el nombre del juego
* **\<plataforma>**: de tipo \<str\>, representa plataforma del lanzamiento de los juegos
* **\<Añodelanzamiento>**: de tipo \<int\>, representa año de lanzamiento del juego
* **\<Editor>**: de tipo \<str\>, representa editor del juego
* **\<NA_Sales>**: de tipo \<float\>, representa ventas en América del Norte (en millones)
* **\<EU_Sales>**: de tipo \<float\>, representa ventas en Europa (en millones)
* **\<JP_Sales>**: de tipo \<float\>, representa ventas en Japón (en millones)
* **\<Other_Sales>**: de tipo \<float\>, representa ventas en el resto del mundo (en millones)
* **\<Global_Sales>**: de tipo \<float\>, representa ventas mundiales totales (en millones)
* **\<Critic_score>**: de tipo \<float\>, representa puntuación agregada compilada por el personal de Metacritic
* **\<Critic_count>**: de tipo \<int\>, representa el número de críticos utilizados para llegar a la puntuación de la crítica
* **\<User_score>**: de tipo \<float\>, representa puntuación de los suscriptores de Metacritic
* **\<User_count>**: de tipo \<int\>, representa número de usuarios que dieron la puntuación de usuario
* **\<Calificación>**: de tipo \<bool\>, representa las calificaciones de esRB


....

## Tipos implementados

Videojuego = namedtuple('Videojuegos', 'Name,Platform,Year_of_Release,Genre,Publisher,NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales,Critic_Score,Critic_Count,User_Score,User_Count,Rating')


## Funciones implementadas
Añade aquí descripciones genéricas de las funciones, que luego debes acompañar con comentarios de tipo documentación en el código

### \<modulo 1\>

* **<def filtra_clasificcion_por_edades(Videojuegos):>**:  La función devuelve una lista con todos los juegos con una clasificación 'everyone', es decir, apto para todos los públicos.

* **<def calcula_media_valoracion_por_juego(videojuegos, name):>**: La función devuelve una lista con la valoración media entre la crítica y los usuarios según el juego seleccionado.

* **<def valor_maximo_ventas_juegos_por_anyo(videojuegos, anyo):>**: La función devuelve una lista con el juego más vendido del año seleccionado.

* **<def agrupa_por_genero(videojuegos, genero):>**: La función devuelve un diccionario con los juegos que pertenecen al género seleccionado.

### \<test modulo 1\>

* **<def test_filtra_clasificcion_por_edades():>**: Descripción de las pruebas realizadas a la función 1.
* **<def test_media_valoracion_por_juegos():>**: Descripción de las pruebas realizadas a la función 2.
* **<def test_valor_maximo_ventas_juegos_por_anyo():>**: Descripción de las pruebas realizadas a la función 1.
* **<def test_agrupa_por_genero(DATOS, accion):>**: Descripción de las pruebas realizadas a la función 2.
* 
### \<modulo 2\>

* **<funcion 1>**: Descripción de la función 1.
* **<funcion 2>**: Descripción de la función 2.
* ...
