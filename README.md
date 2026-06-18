# ConcertMatch

**Título del proyecto**
ConcertMatch

**Autoras:**
Maria Emilia Barbeito, Sofía Belén Bernini, Angelina Marengo, Victoria Mochnacs y Matilde Urrestarazu Romero


**Descripción del proyecto:**

En el panorama actual del entretenimiento, la oferta de música en vivo es masiva y se encuentra fragmentada entre múltiples productoras, estadios y plataformas de venta de entradas. Para los fanáticos de la música, resulta abrumador y tedioso rastrear cada sitio web para encontrar eventos que no solo coincidan con sus gustos musicales, sino que también se ajusten a su presupuesto, horarios disponibles, distancia y otras facilidades.

ConcertMatch busca resolver este problema mediante la centralización de la información en un sistema interactivo que funciona como un "recomendador" de conciertos personalizado. El programa procesaría un Dataset que contenga la información de los eventos musicales disponibles en cartelera, para luego ofrecer recomendaciones precisas según las preferencias del usuario. Estas preferencias serán obtenidas tras una serie de preguntas que se le realizarán al comienzo de su interacción con el programa.

Los filtros que el programa va a aplicar van a ser según las preferencias de género, rango de precios, fecha específica o rango de fechas, franja horaria, distancia máxima dispuesto a recorrer, la disponibilidad de asientos y accesos facilitados para personas con movilidad reducida. 

**Adjudicaciones de partes del programa**
En términos generales, las cinco integrantes del proyecto participamos activamente del diseño del programa general, así como en el diseño de las funciones específicas. Por su parte, Victoria Mochnacs realizó un diagrama de flujo inicial que permitió tener una visualización base del funcionamiento del programa. A su vez, todas nos vimos involucradas en realizar intervenciones a ese diseño si se consideraban pertinentes. Por último, todas estuvimos presentes para corregir los errores que se presentaban en el debugging.

En cuanto a las funciones específicas, quienes estuvieron encargadas de realizar las funciones de "filtrar_df.py" fueron, principalmente, María Emilia Barbeito, Angelina Marengo y Matilde Urrestarazu Romero. 

Por otro lado, las funciones de carga del dataset y su validación y limpieza ("cargar_dataset.py" y "validar_df.py") fueron realizadas principalmente por Sofía Bernini y Victoria Mochnacs. Respecto a las funciones del archivo "pedir_preferencias.py" y al main fue necesaria la participación de todas las partes, ya que contenían funciones y/o bloques de código extensos, por lo que resulta dificil adjudicar esas tareas a una integrante en particular.

Los gráficos de graficos.py y los mensajes de "resultados.py" fueron realizados por Sofía Bernini. No obstante, los gráficos y funciones de "pedir_preferencias.py" que involucraban el funcionamiento de geopy o el cálculo de distancia se le adjudica principalmente a Angelina Marengo

**Descripción de la fuente de datos (en caso de haber utilizado una)**
En nuestro caso particular, utilizamos un mock data de conciertos con datos reales (Artistas, ubicaciones, estadios/predios, links a páginas reales) pero generados con IA para testear el código. Es decir, no utilizamos un Web Scraping de páginas de ticketeras directamente, porque complejizaban de más el desarrollo del proyecto. Además, consideramos que el acceso a esos datos privados podrían estar restringidos y serían dificilmente accesibles mediante Web Scraping.

Sin embargo, hay algunas consideraciones a tener en cuenta sobre los datos que son válidos para el programa, debido a las funciones y librerías que utilizamos. 

Los datos de la columna de Ubicación del Dataset deben tener el nombre completo de la calle (no abreviaciones) y alguna especificación de la ciudad o distrito. Esto debido a que Geopy, la librería que utilizamos para esta validación y para demás funciones, necesita especificidad para hacer correctamente el cálculo de coordenadas de las direcciones. Si no se cargan estos datos correctamente, probablemente se pierdan conciertos en la limpieza de datos, ya que se eliminan las filas que no contengan una ubicación validada por Geopy. O bien, podría perderse alguna de las opciones porque el cálculo de las distancia estaría hecho sobre la dirección de otro distrito o región (Puede haber calles repetidas en distintos distritos).


**Instrucciones para ejecutar el programa**
Para poder ejecutar el programa, se deben tener descargadas las librerías mencionadas en el siguiente apartado. Se pueden descargar recorriendo el archivo requirements.txt

Resulta importante tener en cuenta que el inicio del programa puede tardar algunos segundos/minutos (dependiendo de la cantidad de filas del programa) debido a la validación de ubicaciones que realiza Geopy. Quien ejecute el programa podrá observar un mensaje inicial que dice:

"Comenzando proceso de carga del programa. Podría tardarse unos segundos/minutos. Espere a que aparezca el cartel de inicio del programa"

Luego de la validaciónd el Dataset, aparece el siguiente mensaje de bienvenida, que indica el comienzo del programa:
=============================================
"🎸 BIENVENIDO A CONCERTMATCH 🎸")
=============================================


**Librerías utilizadas:**

* **pandas:** Se utiliza para la carga, limpieza, manipulación y filtrado eficiente del dataset de conciertos.
* **matplotlib.pyplot:** Sirven para la visualización de los datos (gráficos).
* **datetime:** Se utiliza para el procesamiento, parseo y validación de los strings de fechas ingresadas por el usuario frente al calendario de los eventos. Es lo que nos permite saber si la fecha que escribió la persona tiene un formato válido (DD-MM-AAAA).
* **os:** se utiliza en la función cargar\_dataset. Sirve para validar si la ruta del archivo CSV ya existía en la computadora antes de intentar abrirlo, evitando así que el programa colapse de forma inesperada.
* **geopy:** transforma direcciones en coordenadas y calcula distancias.



**Estructura del repositorio:**

Carpetas (Directorios):

* **data:** Almacena el dataset (como archivo CSV).
* **docs:** Contiene la documentación y el diseño (diagramas de flujo) del proyecto.
* **requirements.txt:** En esta carpeta se listan las librerías a instalar (como pandas o matplotlib).
* **src:** Contiene todas las funciones que se van a llamar desde el programa principal.

Archivos en la raíz:

* **.gitignore:** Indica a Github qué archivos o carpetas debe ignorar y no subir al repositorio.
* **README.md:** Es el documento principal de presentación del proyecto.
* **main.py:** Es el punto donde comienza el programa; el archivo principal que ejecuta el código central.




**Uso de Inteligencia Artificial:** (incluir prompts)

Instalación de las librerías externas a Python:
El prompt fue: "Cómo puedo instalar Geopy y Folium en 
