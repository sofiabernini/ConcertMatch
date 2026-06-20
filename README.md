# ConcertMatch

**Título del proyecto:**

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

Matilde Urrestarazu Romero: Diagramas de flujo de las funciones de filtrar y de resultados. Programación de filtrar_df.py, pedir_preferencias.py, resultados.py y colaboración en el armado de la función ejecutar_programa.




**Fuente de Datos:**

El proyecto utiliza un dataset simulado (concertmatch_dataset_prueba.csv) generado con asistencia de Inteligencia Artificial (Gemini). Contiene eventos musicales con información detallada sobre artistas, géneros, precios, fechas, horarios, ubicaciones (direcciones), estadios/predios, disponibilidad de entradas y condiciones del lugar. Además, se incluye información que se mostrará al final o que se filtrará durante la ejecución del programa, como el link que lleva a la ticketera, la fecha en la que se comienzan a vender las entradas para el evento, o la condición de si quedan entradas disponibles. 

Este fue realizado con Inteligencia Artificial (IA) ya que no fue posible acceder a los dataset reales de las ticketeras. De todas formas, el programa está pensado para que se pueda ejecutar si se ingresara un dataset real. Sin embargo, hay algunas consideraciones a tener en cuenta sobre los datos que son válidos para el programa, debido a las funciones y librerías que utilizamos. Por ejemplo, los datos de la columna de Ubicación del dataset deben tener el nombre completo de la calle (no abreviaciones) y alguna especificación de la ciudad o distrito (un ejemplo de formato válido sería escribir "Humboldt 450, CABA"). Esto se debe a que Geopy, la librería que utilizamos para esta validación y para otras funciones, necesita especificidad para hacer correctamente el cálculo de coordenadas de las direcciones. Si no se cargaran correctamente estos datos, probablemente se perderán conciertos a la hora de realizar la limpieza de datos, (ya que se eliminan las filas que no contienen una ubicación validada por Geopy;) o bien, podría perderse alguna de las opciones a mostrar debido a que el cálculo de las distancia estaría hecho sobre la dirección de otro distrito o región (puede haber calles repetidas en distintos distritos).

Aclaración: El dataset no llega a los 1000 registros (como se indica en la consigna) porque la IA no fue capaz de realizarlo. Sin embargo, esto ya fue conversado y aprobado por los profesores.




**Instrucciones para ejecutar el programa**

Para poder ejecutar el programa, se deben tener descargadas las librerías mencionadas en el siguiente apartado. También se pueden ver en el archivo requirements.txt

Resulta importante tener en cuenta que el inicio del programa puede tardar algunos segundos/minutos (dependiendo de la cantidad de filas del programa) debido a la validación de ubicaciones que realiza Geopy. Quien ejecute el programa podrá observar un mensaje inicial que dice:

"Comenzando proceso de carga del programa. Podría tardarse unos segundos/minutos. Espere a que aparezca el cartel de inicio del programa"

Luego de la validación del dataset, aparece el siguiente mensaje de bienvenida, que indica el comienzo del programa:

=============================================
"🎸 BIENVENIDO A CONCERTMATCH 🎸")
=============================================

Otra aclaración importante a tener en cuenta con respecto a las condiciones necesarias para la correcta ejecución del programa es que la geolocalización requiere conexión a internet para conectarse a OpenStreetMap mediante Geopy.




**Librerías utilizadas:**

* **pandas:** Se utiliza para la carga, limpieza, manipulación y filtrado eficiente del dataset de conciertos.
* **matplotlib.pyplot:** Sirven para la generación del histograma comparativo.
* **datetime:** Se utiliza para el procesamiento, parseo y validación de los strings de fechas ingresadas por el usuario frente al calendario de los eventos. Es lo que nos permite saber si la fecha que escribió la persona tiene un formato válido (DD-MM-AAAA).
* **os:** se utiliza en la función cargar_dataset. Sirve para validar si la ruta del archivo CSV ya existía en la computadora antes de intentar abrirlo, evitando así que el programa colapse de forma inesperada.
* **geopy:** Realiza la geolocalización para convertir la dirección ingresada por el usuario en coordenadas (latitud/longitud) y el cálculo de distancias reales con geodesic.
* **webbrowser:** Permite abrir un archivo .html en la ventana del navegador
* **folium**: Permite la creación del mapa interactivo HTML con marcadores agrupados (MarkerCluster).
* **time**: Se utiliza para castear el formato de horario y fechas. También, para que la geolocalización de la columna "Ubicación" no se sature


*Aclaraciones sobre Geopy*
Es importante remarcar que para calcular la distancia entre la ubicación de partida del usuario y la distancia del evento, como mencionamos, utilizamos la función 'geodesic()'. Esta función calcula la distancia geodésica, es decir, la distancia en línea recta entre dos coordenadas (considerando la curvatura de la Tierra), y no la distancia real de viaje por calles, rutas o caminos. 

Esto significa que la distancia mostrada por el programa puede ser menor a la distancia que efectivamente se recorrería a pie o en auto entre ambos puntos. Si bien podría considerarse una limitación para el proyecto, lo elegimos porque de otra forma habría que utilizar APIs (como OpenRouteService o Google Distance Matrix), que tienen un límite de consultas diarias o mensuales.




**Estructura del repositorio:**

Carpetas (Directorios):

* **data:** Almacena el dataset en concertmatch_dataset_prueba.csv
* **docs:** Contiene los diagramas de flujo de las funciones del proyecto y el Prompt base (utilizado para dar contexto a la hora de consultar a la Inteligencia Artificial).
* **requirements.txt:** En esta carpeta se listan las librerías que se deben instalar para poder ejecutar el programa (pandas, matplotlib.pyplot, datetime, os, geopy, folium, webbrowser, time)
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




**Uso de Inteligencia Artificial:** 

La Inteligencia Artificial (IA) fue utilizada como herramienta de apoyo durante el desarrollo, puntualmente para la generación de datos, la prevención de errores y la creación de la estructura básica de determinadas funciones. Todas las respuestas que fueron dadas, luego fueron perfeccionadas y modificadas según fuera necesario. Los nuevos prompts que fuimos generando se basaron en el contexto ya otorgado por el "Prompt base" (que se puede visualizar dentro de la carpeta de "docs" en el repositorio. A continuación, mostraremos algunos de los prompts más importantes junto a breve descripciones de para qué fueron utilizados:

- Funciones pedir_ubicacion_partida y calcular_distancias: 
Prompt 1:
"Estamos haciendo un trabajo aplicado de Programación. Prompt base. Para la categoría “distancia” necesito calcular distancias entre la ubicación del usuario y cada una de las ubicaciones del DataFrame. Por lo tanto, necesito que me recomiendes una librería/API que me permita calcular distancias."

Prompt 2:
"Ahora que me recomendaste usar la librería geopy, necesito que me armes un código que: i) le pida al usuario su dirección ii) permita calcular distancias entre la ubicación del usuario y cada una de las ubicaciones del DataFrame. iii) Luego, guarde las distancias en una lista de distancias  iv) agregue lista_distancias al DataFrame como una columna de “distancias”. 
Necesito que esto esté dentro de funciones, pueden ser las que consideres necesarias para que no queden funciones con muchas responsabilidades. Además, necesito que me expliques de manera exhaustiva y precisa qué es lo que hace cada bloque de código, porque necesito entender bien qué es lo me permite hacer esta librería."


- pedir_generos:
Prompt: "Necesito que generes una función que pida los géneros que le agradan al usuario. La función debe recibir por parámetro una columna de géneros de un DataFrame, eliminar los géneros repetidos y mostrarle al usuario una tabla con el ID de cada género y el género asociado para que el usuario seleccione uno o más ingresando sus ID hasta que ingrese ‘fin’. Maneja todos los errores que puedan surgir en la interacción con el usuario y finalmente debe devolver una lista con los géneros seleccionados."


- Para la función pedir fechas() se usó la Inteligencia Artificial, especialmente para la conversión de los datos ingresados por el usuario a objetos de mediante la libreria datetime y el manejo de los errores relacionados con el ingreso de las fechas. Al igual que en pedir_franja_horaria () donde se la utilizó para resolver dudas concretas sobre el formato y la construcción de las variables hora_min y hora_max.


- grafico_mapa: 
Prompt 1: “Necesito que hagas una función que cree un gráfico de mapa de los eventos que quedaron en df_ordenado utilizando la librería folium. La función debe: Recibir el df_ordenado por parámetro, Verificar que el df_ordenado no esté vacío, Crear un mapa interactivo:
deben estar los eventos del df_ordenado representados con marcadores en el mapa al tocar cada marcado debe saltar la información del evento”

Luego, simplemente queríamos agregar que, al crear el gráfico del mapa, se abriera una pestaña web automáticamente. Entonces:

Prompt 2: "¿Hay forma de que el html de mapa se muestre en Spyder? ¿o solo se muestra aparte (en un archivo creado automáticamente? ¿cómo puedo hacer para que se visualice de una forma más cómoda para el usuario? La respuesta que nos dio fue la misma que incorporamos al código del programa."


- resultados:
En la función de ordenar_resultados() se utilizó la IA con el siguiente Prompt: Hacer una función que reciba por parámetro un df filtrado y el nombre de una columna y que ordene los conciertos de menor a mayor según esa columna. Finalmente devolver el DataFrame ordenado. 

En la funcion mostrar_info_resultados(df_ordenado) se utilizó la IA especialmente para la línea: for _, fila in df_ordenado.head(5).iterrows(): para evitar generar otro DataFrame que solo contenga los 5 primeros conciertos y poder recorrer directamente el df_ordenado que devolvió la función anterior.


- crear_histograma_comparativo: 
Prompt: "Necesito que hagas una función que cree un histograma comparativo entre: 
El df original que contiene todos los eventos
El df_filtrado, que es el df resultado de aplicar todos los filtros
La idea de esta función es que recibe por parámetro una variable llamada columna_importante, y que en base a esta haga el histograma de la siguiente manera:
si columna_importante es igual a “Precio final”, entonces el histograma debe mostrar la cantidad de conciertos de ambos df para los distintos rangos de precios. 
si columna_importante es igual a “distancias”, entonces el histograma debe mostrar la cantidad de conciertos de ambos df para las distintas distancias. 
Algunas aclaraciones importantes: 
columna_importante sí o sí es “Precio final” o “distancias”. No puede valer otra cosa, porque existe una función llamada obtener_columna_importante que se fija si “precio” o “distancia” está antes que la otra en categorias_ordenadas y en base a eso devuelve “Precio final” o “distancia” respectivamente. Por lo tanto, no es necesario validar el valor de la variable columna_importante.
El histograma debe superponer la información de ambos DataFrames para que el usuario pueda visualizar cómo quedaron los conciertos recomendados respecto del conjunto total de conciertos disponibles."


- Creación de dataset:
Al no poder acceder a los datasets reales de las ticketeras, le pedimos a la Inteligencia Artificial que generara uno con el que pudiéramos trabajar. El prompt fue el siguiente:
“Generá un dataset que contenga las siguiente columnas: Artista/Banda, Género musical, Precio final, Fecha, Horario, Ubicación (dirección), Estadio/Predio, Acceso movilidad reducida (True/False), Lugar para sentarse (True/False), Link ticketera, Quedan entradas (True/False), Lanzamiento venta (con una fecha asignada). 
El Dataset debe tener la mayor cantidad de filas posibles (idealmente 1000) y debe basarse en información real de eventos que estén a la venta actualmente.”


- Manejo de errores en función carga_dataset:
Dado que no profundizamos en el manejo de datasets durante las clases, quisimos anticipar posibles fallos desconocidos. Por ello, consultamos a la Inteligencia Artificial sobre cómo prevenir errores al cargar y procesar los datos en el programa. El prompt fue el siguiente:
“Necesito que, como si fueras un programador experto, generes una función llamada carga_dataset que reciba por parámetro una ruta de archivo CSV (llamado ruta_archivo), lo abra y lo convierta en un DataFrame de pandas. Además, agregale toda la prevención de errores necesaria (usando try-except o validaciones) para atajar cualquier problema antes de que ocurra (por ejemplo: que el archivo no exista, que el dataset esté completamente vacío, que no tengamos los permisos para acceder al dataset, etc.). La idea es que el programa sea robusto y no se rompa.”


- Funciones de validar_df:
Al tener que validar las ubicaciones, tuvimos que preguntarle a la IA cómo utilizar Geopy para obtener las coordenadas de la columna “Ubicación”, crear las columnas de longitud y latitud, y asignarles Nan si no se encontraba alguna de las ubicaciones:

Prompt: “Tengo este dataset y quiero validar que las Ubicaciones (columna "Ubicación") existan, usando geopy, dentro de una función que se llama "limpieza_df". Mi idea es verificar que las direcciones existan y, si alguna no existe, convertir ese dato a NaN. Al final de la función de limpieza, simplemente voy a hacer un df = df.dropna(). ¿Qué recomendarías que haga?” (Cargué el mock data)

Este prompt tuvo sus modificaciones y finalmente fue utilizado para la función “limpiar_ubicaciones”
A su vez, utilice la IA para implementar ciertas validaciones de horario o fechas, y me sugirió incorporar la librería time. Por último, la IA me recomendó hacer la limpieza de valores booleanos con .map.



