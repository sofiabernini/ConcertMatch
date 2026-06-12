# ConcertMatch

Autoras:
Maria Emilia Barbeito, Sofía Belén Bernini, Angelina Marengo, Victoria Mochnacs y Matilde Urrestarazu Romero


Descripción del proyecto:

En el panorama actual del entretenimiento, la oferta de música en vivo es masiva y se encuentra fragmentada entre múltiples productoras, estadios y plataformas de venta de entradas. Para los fanáticos de la música, resulta abrumador y tedioso rastrear cada sitio web para encontrar eventos que no solo coincidan con sus gustos musicales, sino que también se ajusten a su presupuesto, horarios disponibles y distancia.

ConcertMatch busca resolver este problema mediante la centralización de la información en un sistema interactivo que funciona como un "recomendador" de conciertos personalizado. El programa procesaría un dataset que contenga la información de los eventos musicales disponibles en cartelera, para luego ofrecer recomendaciones precisas según las preferencias del usuario. Estas preferencias serán obtenidas tras una serie de preguntas que se le realizarán al comienzo de su interacción con el programa.


Librerías utilizadas:

pandas: Se utiliza para la carga, limpieza, manipulación y filtrado eficiente del dataset de conciertos.
matplotlib.pyplot: Sirven para la visualización de los datos (gráficos).
datetime: Se utiliza para el procesamiento, parseo y validación de los strings de fechas ingresadas por el usuario frente al calendario de los eventos. Es lo que nos permite saber si la fecha que escribió la persona tiene un formato válido (DD-MM-AAAA).
os: se utiliza en la función cargar_dataset. Sirve para validar si la ruta del archivo CSV ya existía en la computadora antes de intentar abrirlo, evitando así que el programa colapse de forma inesperada.
geopy: transforma direcciones en coordenadas y calcula distancias.


Estructura del repositorio:





Uso de Inteligencia Artificial: (incluir prompts)
