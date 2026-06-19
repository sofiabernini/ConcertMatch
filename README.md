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

Luego de la validación el Dataset, aparece el siguiente mensaje de bienvenida, que indica el comienzo del programa:
=============================================
"🎸 BIENVENIDO A CONCERTMATCH 🎸")
=============================================


**Librerías utilizadas:**

* **pandas:** Se utiliza para la carga, limpieza, manipulación y filtrado eficiente del dataset de conciertos.
* **matplotlib.pyplot:** Sirven para la visualización de los datos (gráficos).
* **datetime:** Se utiliza para el procesamiento, parseo y validación de los strings de fechas ingresadas por el usuario frente al calendario de los eventos. Es lo que nos permite saber si la fecha que escribió la persona tiene un formato válido (DD-MM-AAAA).
* **os:** se utiliza en la función cargar\_dataset. Sirve para validar si la ruta del archivo CSV ya existía en la computadora antes de intentar abrirlo, evitando así que el programa colapse de forma inesperada.
* **geopy:** Transforma direcciones en coordenadas y calcula distancias.

*Aclaraciones sobre Geopy*
Es importante remarcar que, para calcular la distancia entre la ubicación de partida del usuario y la distancia del evento, utilizamos la función 'geodesic()'. Esta función calcula la distancia geodésica, es decir, la distancia en línea recta entre dos coordenadas (considerando la curvatura de la Tierra), y no la distancia real de viaje por calles, rutas o caminos. 

Esto significa que la distancia mostrada por el programa puede ser menor a la distancia que efectivamente se recorrería a pie o en auto entre ambos puntos. Si bien podría considerarse una limitación para el proyecto, lo elegimos porque de otra forma habría que utilizar APIs (como OpenRouteService o Google Distance Matrix), que tienen un límite de consultas diarias o mensuales.




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

-- Instalación de las librerías externas a Python:--
IA utilizada: *Claude*
Quienes utilizamos el prompt: Victoria y Emilia (usuarias de Mac)

El prompt fue: "Cómo instalo geopy desde la terminal de mi mac? paso a paso (desde cómo ir a la carpeta)"

Lo primero que me respondió fue:
    "Antes de darte los pasos, ¿ya tenés un entorno virtual creado para el proyecto, o estás instalando todo de forma global?" 

Al no saber qué era un entorno virtual, le pedí que me explicara:

    "Un entorno virtual es una carpeta que contiene una instalación de Python aislada para tu proyecto. Sirve para que las librerías que instalás (como geopy) no se mezclen con otras instalaciones de Python que tengas en tu computadora.
    
    Te recomiendo crearlo antes de instalar nada. Los pasos serían:

    1. Abrís la terminal (la buscás en Spotlight con Cmd + Space y escribís "Terminal")
    2. Navegás a la carpeta de tu proyecto:
    cd ruta/de/tu/proyecto
    3. Creás el entorno virtual:
    python3 -m venv venv
    4. Activás el entorno virtual:
    source venv/bin/activate
    5. Instalás geopy:
    pip install geopy"

Después de realizar esta secuencia de pasos, todavía no me dejaba utilizar Geopy, entonces le consulté, y me dijo:

    "El problema es que instalaste geopy en el entorno virtual pero tu programa está corriendo fuera de él. Cada vez que abrís una terminal nueva o un IDE nuevo, el entorno virtual se desactiva.

    En Spyder tenés que cambiar el intérprete de Python. Los pasos son:
    1. Arriba en el menú vas a Tools → Preferences
    2. En el panel izquierdo clickeás Python interpreter
    3. En "Use the following interpreter" pegás esta ruta:
    /Users/victoriamochnacs/Documents/GitHub/ConcertMatch/venv/bin/python
    4. Apretás Apply y OK
    5. Spyder te va a pedir que reinincies el kernel, aceptás.
    Después de eso debería funcionar el import geopy."

Me surgió un problema con lo que me decía del kernel, así que volví a consultar y contestó esto:

    "Tenés que instalar spyder kernels"
    pip install "spyder-kernels==3.0.*""

Luego, no entendía por qué Spyder no reconocía pandas o matplotlib como librerías ya instaladas. Lo que me sugirió fue instalarlas en el entorno virtual. Por último, en GitHub Desktop me aparecían alrededor de 9000 commits para hacer, y consulté a qué se debía:

    "No hagas el commit todavía! El problema es que la carpeta venv está dentro de tu repositorio y Git la está trackeando. Son 9536 archivos porque un entorno virtual contiene muchísimos archivos internos de Python que no deberían subirse a GitHub.
    La solución es agregar venv al .gitignore antes de commitear:
    1. Abrí el archivo .gitignore que está en la raíz de tu proyecto (si no existe, crealo)
    2. Agregá estas líneas:
    cd "/Users/victoriamochnacs/Documents/GitHub/ConcertMatch"
    echo "venv/" >> .gitignore"

Finalmente, pude instalar las librerías sin ningún problema

