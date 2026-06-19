# ConcertMatch

**Título del proyecto**
🎸 ConcertMatch: Recomendador Inteligente de Conciertos 

**Autoras:**
María Emilia Barbeito, Sofía Belén Bernini, Angelina Marengo, Victoria Mochnacs y Matilde Urrestarazu Romero


**Objetivo y descripción general del funcionamiento del sistema:**

En el panorama actual del entretenimiento, la oferta de música en vivo es masiva y se encuentra fragmentada entre múltiples productoras, estadios y plataformas de venta de entradas. Para los fanáticos de la música, puede resultar abrumador y tedioso rastrear cada sitio web para encontrar eventos que no solo coincidan con sus gustos musicales, sino que también se ajusten a su presupuesto, horarios disponibles, distancia y otras facilidades.

ConcertMatch busca resolver este problema mediante la centralización de la información en un sistema interactivo que funciona como un "recomendador" de conciertos personalizado. El programa procesa un Dataset que contiene la información de los eventos musicales disponibles en cartelera, para luego ofrecer recomendaciones precisas según las preferencias del usuario (género musical, presupuesto, disponibilidad horaria y de fechas, distancia máxima a recorrer y necesidades de accesibilidad/asientos). Estas preferencias serán obtenidas tras una serie de preguntas que se le realizarán al comienzo de su interacción con el programa.

Finalmente, el usuario verá sus resultados en tres formatos distintos. El primero será por medio de la consola, donde se imprimirá un listado ordenado y detallado con los mejores conciertos recomendados que se ajustan a los filtros que se fueron aplicando. El segundo formato consistirá en un histograma comparativo, el cual le permitirá analizar visualmente cómo se distribuyen sus opciones recomendadas frente al total de la oferta (enfocándose en su variable de mayor prioridad, ya sea el precio o la distancia). Por último, el programa generará y abrirá automáticamente un mapa interactivo en su navegador web, donde podrá explorar la ubicación geográfica exacta de cada evento sugerido haciendo clic en los marcadores.


**Adjudicación de tareas:** 

Las cinco integrantes del proyecto participamos activamente en el diseño del programa (armado de la propuesta y diagramas de flujo), el armado de las funciones y el manejo de errores. Sin embargo, podríamos asignar las siguientes tareas a las siguientes colaboradoras:

Maria Emilia Barbeito: Programación de la funcion ordenar_preferencias, diagramas de flujo del archivo pedir_prefrencias.

Sofía Belén Bernini: Armado del dataset simulado (concertmatch_dataset_prueba.csv), creación y organización de la estructura del repositorio, redacción del README. Además, la programación de las funciones carga_dataset, filtrar_df_bool, hacer_pregunta_si_no, pedir_lugar_para_sentarse, mostrar_info_resultados, y gran parte de ejecutar_programa.

Angelina Marengo: Programación de las funciones dentro del archivo pedir_preferencias, graficos.py, filtrar_df.py. Diagramas de flujo del archivo pedir_preferencias.

Victoria Mochnacs: Diagrama inicial del programa general. Programación de las funciones dentro de validar_df.py, pedir_preferencias.py.

Matilde Urrestarazu Romero: Programación de pedir_preferencias.py, filtrar_df.py y resultados.py




#Redactar mejor
**Fuente de Datos:**

El proyecto utiliza un dataset simulado (concertmatch_dataset_prueba.csv) generado con asistencia de Inteligencia Artificial (Gemini). Contiene eventos musicales con información detallada sobre artistas, géneros, precios, fechas, horarios, ubicaciones (direcciones), estadios/predios, disponibilidad de entradas y condiciones del lugar. Además, se incluye información que se mostrará al final o que se filtrará durante la ejecución del programa, como el link que lleva a la ticketera, la fecha en la que se comienzan a vender las entradas para el evento, o la condición de si quedan entradas disponibles. 

Este fue realizado con Inteligencia Artificial (IA) ya que no fue posible acceder a los dataset reales de las ticketeras. De todas formas, el programa está pensado para que se pueda ejecutar si se ingresara un dataset real. Sin embargo, hay algunas consideraciones a tener en cuenta sobre los datos que son válidos para el programa, debido a las funciones y librerías que utilizamos. Por ejemplo, los datos de la columna de Ubicación del dataset deben tener el nombre completo de la calle (no abreviaciones) y alguna especificación de la ciudad o distrito. Esto se debe a que Geopy, la librería que utilizamos para esta validación y para otras funciones, necesita especificidad para hacer correctamente el cálculo de coordenadas de las direcciones. Si no se cargan estos datos correctamente, probablemente se pierdan conciertos en la limpieza de datos, ya que se eliminan las filas que no contengan una ubicación validada por Geopy. O bien, podría perderse alguna de las opciones porque el cálculo de las distancia estaría hecho sobre la dirección de otro distrito o región (puede haber calles repetidas en distintos distritos).

Aclaración: El dataset no llega a los 1000 registros (como se indica en la consigna) porque la IA no fue capaz de realizarlo. Sin embargo, esto ya fue conversado y aprobado por la profesora.


#ver si esto al final va a ser así según si podemos mejorar lo de Geopy
**Instrucciones para ejecutar el programa**

Para poder ejecutar el programa, se deben tener descargadas las librerías mencionadas en el siguiente apartado. También se pueden ver en el archivo requirements.txt

Resulta importante tener en cuenta que el inicio del programa puede tardar algunos segundos/minutos (dependiendo de la cantidad de filas del programa) debido a la validación de ubicaciones que realiza Geopy. Quien ejecute el programa podrá observar un mensaje inicial que dice:

"Comenzando proceso de carga del programa. Podría tardarse unos segundos/minutos. Espere a que aparezca el cartel de inicio del programa"

Luego de la validación el Dataset, aparece el siguiente mensaje de bienvenida, que indica el comienzo del programa:
=============================================
"🎸 BIENVENIDO A CONCERTMATCH 🎸")
=============================================


**Librerías utilizadas:**

* **pandas:** Se utiliza para la carga, limpieza, manipulación y filtrado eficiente del dataset de conciertos.
* **matplotlib.pyplot:** Sirven para la generación del histograma comparativo.
* **datetime:** Se utiliza para el procesamiento, parseo y validación de los strings de fechas ingresadas por el usuario frente al calendario de los eventos. Es lo que nos permite saber si la fecha que escribió la persona tiene un formato válido (DD-MM-AAAA).
* **os:** se utiliza en la función cargar_dataset. Sirve para validar si la ruta del archivo CSV ya existía en la computadora antes de intentar abrirlo, evitando así que el programa colapse de forma inesperada.
* **geopy:** Realiza la geolocalización para convertir la dirección ingresada por el usuario en coordenadas (latitud/longitud) y el cálculo de distancias reales con geodesic.
* **webbrowser:** Permite abrir un archivo .html en la ventana del navegador
* **folium**: Permite la creación del mapa interactivo HTML con marcadores agrupados (MarkerCluster).


*Aclaraciones sobre Geopy*
Es importante remarcar que para calcular la distancia entre la ubicación de partida del usuario y la distancia del evento, como mencionamos, utilizamos la función 'geodesic()'. Esta función calcula la distancia geodésica, es decir, la distancia en línea recta entre dos coordenadas (considerando la curvatura de la Tierra), y no la distancia real de viaje por calles, rutas o caminos. 

Esto significa que la distancia mostrada por el programa puede ser menor a la distancia que efectivamente se recorrería a pie o en auto entre ambos puntos. Si bien podría considerarse una limitación para el proyecto, lo elegimos porque de otra forma habría que utilizar APIs (como OpenRouteService o Google Distance Matrix), que tienen un límite de consultas diarias o mensuales.




**Estructura del repositorio:**

Carpetas (Directorios):

* **data:** Almacena el dataset en concertmatch_dataset_prueba.csv
* **docs:** Contiene la documentación y el diseño (diagramas de flujo) del proyecto.
* **requirements.txt:** En esta carpeta se listan las librerías que se deben instalar para poder ejecutar el programa (pandas, matplotlib.pyplot, datetime, os, geopy, folium, webbrowser
* **src:** Contiene todas las funciones que se van a llamar desde el programa principal (dentro de los archivos: cargar_dataset.py, filtrar_df.py, graficos.py, pedir_preferencias.py, resultados.py, validar_df.py)

Archivos en la raíz:

* **.gitignore:** Indica a Github qué archivos o carpetas debe ignorar y no subir al repositorio.
* **README.md:** Es el documento principal de presentación del proyecto.
* **main.py:** Es el punto donde comienza el programa; el archivo principal que ejecuta el código central.
* **mapa_conciertos.html:** Es el archivo generado automáticamente por la función que genera el mapa (en graficos.py)



**Funciones principales:**
carga_dataset(): Carga el archivo CSV manejando errores específicos (archivos inexistentes, corruptos o sin permisos) y ejecuta la validación.

validar_df: Llama a las funciones "validar_columnas" y "limpiar_df". Estas validan la cantidad de columnas del DataFrame,evalúan el rango de precios, castean fechas/horarios, corrigen str a valores booleanos, geolocalizan las direcciones de la columna ["Ubicación"] y eliminan valores inconsistentes (Nan).

pedir_preferencias(): Hace las preguntas al usuario (género, rango de precios, franja horaria, fecha o rango de fechas, disponibilidad de asientos, distancia máxima y ubicación) y calcula la distancia geolocalizada desde el punto de partida usando la librería Geopy (que utiliza la API OpenStreetMap).

aplicar_filtros(): Aplica iterativamente los filtros seleccionados respetando el orden de prioridad definido por el usuario. Tiene la robustez de frenar y avisar si un filtro elimina todas las opciones.

grafico_mapa() y crear_histograma_comparativo(): Toman el DataFrame resultante para generar un HTML interactivo y un gráfico de barras (histograma), respectivamente.



**Resultados, Outputs y Gráficos:**

Para la visualización de los resultados, el programa ofrece tres formatos distintos:
1) Ranking por Consola: Imprime de manera prolija la información detallada de los mejores conciertos encontrados.
2) Histograma Comparativo: Muestra cómo se distribuyen los conciertos recomendados respecto al total de la oferta según la variable más importante para el usuario (precio o distancia).
3) Mapa Interactivo: Un archivo .html que se abre automáticamente en el navegador, mostrando la ubicación exacta de los eventos recomendados, con popups informativos y clústeres para estadios con múltiples fechas.



**Diagramas de diseño:**

Los diagramas de flujo, donde se permite una mejor visualización del orden de ejecución del programa y de las funciones, pueden ser vistos en los archivos dentro de la carpeta "docs".



**Uso de Inteligencia Artificial:** (incluir prompts)

La Inteligencia Artificial fue utilizada como herramienta de apoyo durante el desarrollo, puntualmente para:

- Generación de Datos: Creación de la estructura y el contenido simulado del dataset de conciertos.

- Mejoras en el diseño: Por ejemplo, se pidieron diversos emojis tales como: 🎸


-- Instalación de las librerías externas a Python:--
IA utilizada: *Claude*
Quienes utilizamos el prompt: Victoria y Emilia (usuarias de Mac)

El prompt fue: "Cómo instalo geopy desde la terminal de mi mac? paso a paso (desde cómo ir a la carpeta)"

Lo primero que respondió fue:
    "Antes de darte los pasos, ¿ya tenés un entorno virtual creado para el proyecto, o estás instalando todo de forma global?" 

Al no saber qué era un entorno virtual, le pedimos que nos explicara:

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

Después de realizar esta secuencia de pasos, todavía no nos dejaba utilizar Geopy, entonces le consultamos, y nos dijo:

    "El problema es que instalaste geopy en el entorno virtual pero tu programa está corriendo fuera de él. Cada vez que abrís una terminal nueva o un IDE nuevo, el entorno virtual se desactiva.

    En Spyder tenés que cambiar el intérprete de Python. Los pasos son:
    1. Arriba en el menú vas a Tools → Preferences
    2. En el panel izquierdo clickeás Python interpreter
    3. En "Use the following interpreter" pegás esta ruta:
    /Users/victoriamochnacs/Documents/GitHub/ConcertMatch/venv/bin/python
    4. Apretás Apply y OK
    5. Spyder te va a pedir que reinincies el kernel, aceptás.
    Después de eso debería funcionar el import geopy."

Surgió un problema con lo que decía del kernel, así que volvimos a consultar y contestó lo siguiente:

    "Tenés que instalar spyder kernels"
    pip install "spyder-kernels==3.0.*""

Luego, no entendíamos por qué Spyder no reconocía pandas o matplotlib como librerías ya instaladas. Lo que nos sugirió fue instalarlas en el entorno virtual. Por último, en GitHub Desktop aparecían alrededor de 9000 commits para hacer, y consultamos a qué se debía:

    "No hagas el commit todavía! El problema es que la carpeta venv está dentro de tu repositorio y Git la está trackeando. Son 9536 archivos porque un entorno virtual contiene muchísimos archivos internos de Python que no deberían subirse a GitHub.
    La solución es agregar venv al .gitignore antes de commitear:
    1. Abrí el archivo .gitignore que está en la raíz de tu proyecto (si no existe, crealo)
    2. Agregá estas líneas:
    cd "/Users/victoriamochnacs/Documents/GitHub/ConcertMatch"
    echo "venv/" >> .gitignore"

Finalmente, se pudieron instalar las librerías sin ningún problema

-- Gráfico de mapa interactivo --
Simplemente queríamos agregar que, al crear el gráfico del mapa, se abriera una pestaña web automáticamente.

Prompt: "¿Hay forma de que el html de mapa se muestre en Spyder? ¿o solo se muestra aparte (en un archivo creado automáticamente? ¿cómo puedo hacer para que se visualice de una forma más cómoda para el usuario?

Respuesta: 
    "Se pueden agregar estas líneas de código para que el archivo .html se abra directamente en el navegador"
    
    import webbrowser
    import os

    def grafico_mapa(df_mejores):
        # ... todo tu código existente ...
        
        mapa.save("mapa_conciertos.html")
        print("Mapa generado correctamente: mapa_conciertos.html")
        
        ruta_completa = os.path.abspath("mapa_conciertos.html")
        webbrowser.open(f"file://{ruta_completa}")



**Aclaraciones finales para la correcta ejecución del programa:**

- La geolocalización requiere conexión a internet para conectarse a OpenStreetMap mediante geopy.

