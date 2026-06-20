#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 20:28:55 2026

@author: victoriamochnacs
"""

import matplotlib.pyplot as plt
import os
import webbrowser
import folium
from folium.plugins import MarkerCluster

def grafico_mapa(df):
    """
    Genera un mapa interactivo con los conciertos recomendados al usuario.
    Cada concierto aparece como un marcador y, al hacer clic sobre él,
    se muestra información relevante del evento.

    Parameters:
    df_resultados (DataFrame) - DataFrame que contiene los conciertos
    filtrados o recomendados.
    
    Returns:
    None.
    Genera un archivo HTML llamado "mapa_conciertos.html".
    """ 
    # Obtener las coordenadas del primer concierto para centrar inicialmente el mapa
    latitud_centro = df.iloc[0]["latitud"]
    longitud_centro = df.iloc[0]["longitud"]
    
    # Crear el mapa base
    mapa = folium.Map(location=[latitud_centro, longitud_centro], zoom_start=11)
    
    # CREAR EL CLUSTER: Esto evita que los marcadores en un mismo estadio/predio se tapen
    cluster = MarkerCluster().add_to(mapa)
    
    for _, fila in df.iterrows():
        
        # CORRECCIÓN DE POPUP: Concatenamos los strings con '+' y quitamos las comas 
        # al final de cada renglón para que Python no lo interprete como una tupla.
        texto_popup = (
            f"<b>Artista: {fila['Artista/Banda']}</b><br>" +
            f"Fecha: {fila['Fecha']}<br>" +
            f"Precio: ${fila['Precio final']}<br>" +
            f"Lugar: {fila['Estadio/Predio']}"
        )
        
        # Crear marcador para el concierto actual
        marcador = folium.Marker(
            location=[fila["latitud"], fila["longitud"]],
            popup=folium.Popup(texto_popup, max_width=300)
        )
    
        # AGREGAR AL CLUSTER en lugar de directo al mapa
        marcador.add_to(cluster)
      
    # Guardar en carpeta específica y abrir en web browser
    #Crear carpeta 
    carpeta_destino = "graficos/"
    os.makedirs(carpeta_destino, exist_ok=True)
    
    ruta_archivo = os.path.join(carpeta_destino, "mapa_conciertos.html")

    mapa.save(ruta_archivo)
    print(f"Mapa generado correctamente: {ruta_archivo}")

    ruta_completa = os.path.abspath(ruta_archivo)
    webbrowser.open(f"file://{ruta_completa}")
   
   

def crear_histograma_comparativo(df_original, df_filtrado, columna_importante):
    """
    Descripción:
    Genera un histograma comparativo entre el dataset original y el
    dataset filtrado utilizando la variable más importante para el usuario.

    El gráfico permite visualizar cómo se distribuyen los conciertos
    recomendados respecto del total de conciertos disponibles en el
    dataset.

    Parámetros:
    df_original (DataFrame) - dataset completo cargado al inicio
    del programa.

    df_filtrado (DataFrame) - dataset resultante luego de aplicar
    todos los filtros seleccionados por el usuario.

    columna_importante (str) - nombre de la columna que se utilizará
    para realizar la comparación. Puede ser:
    - "Precio final"
    - "distancias"

    Retorno:
    None. La función muestra un histograma comparativo en pantalla.
    """

    # Determina qué columna del DataFrame se utilizará
    if columna_importante == "Precio final":
        titulo = "Distribución de precios" #determina el título del gráfico
        nombre_archivo = "histograma_precios"

    elif columna_importante == "distancias":
        titulo = "Distribución de distancias"#determina el título del gráfico
        nombre_archivo = "histograma_distancias"

    # Crear la figura donde se dibujará el gráfico
    plt.figure(figsize=(10, 6))

    # Histograma del dataset original
    plt.hist(
        df_original[columna_importante],
        bins=10,
        alpha=0.5,
        label="Todos los conciertos"
    )

    # Histograma del dataset filtrado
    plt.hist(
        df_filtrado[columna_importante],
        bins=10,
        alpha=0.7,
        label="Conciertos recomendados"
    )

    # Etiqueta del eje X
    plt.xlabel(columna_importante)

    # Etiqueta del eje Y
    plt.ylabel("Cantidad de conciertos")

    # Título del gráfico
    plt.title(titulo)

    # Mostrar leyenda
    plt.legend()

    # Ajustar márgenes automáticamente
    plt.tight_layout()
    
    # Guardar el gráfico en la carpeta de gráficos
    carpeta_destino = "graficos"
    os.makedirs(carpeta_destino, exist_ok=True)

    # --- Guardar la figura dentro de esa carpeta ---
    ruta_archivo = os.path.join(carpeta_destino, nombre_archivo)
    plt.savefig(ruta_archivo)
    print(f"Histograma guardado correctamente: {ruta_archivo}")

    # Mostrar el gráfico
    plt.show()
   
   
   
   
   
   
   
   
   
   
