#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 20:28:55 2026

@author: victoriamochnacs
"""

# FUNCIÓN PARA MOSTRAR EL GRÁFICO CON LOS PORCENTAJES DE COINCIDENCIA
import matplotlib.pyplot as plt
import folium

def grafico_resultado(df_mejores):
    """
    Muestra un gráfico de barras horizontales con los mejores resultados.
    """
    if df_mejores.empty:
        return
        
    plt.figure(figsize=(10, 6))
    
    # Creamos el gráfico de barras horizontales
    bars = plt.barh(df_mejores['Artista/Banda'], df_mejores['porcentaje_coincidencia'], color='mediumpurple') 
    
    plt.xlabel('Porcentaje de Coincidencia (%)', fontweight='bold')
    plt.ylabel('Artista / Banda', fontweight='bold')
    plt.title('Top Recomendaciones - ConcertMatch', fontsize=14, fontweight='bold')
    plt.xlim(0, 105) # Damos un poco de margen visual más allá del 100%
    
    # Invertimos el eje Y para que el resultado con mayor coincidencia quede arriba
    plt.gca().invert_yaxis()
    
    # Agregamos el número del porcentaje al lado de cada barra
    for bar in bars:
        ancho = bar.get_width()
        plt.text(ancho + 1.5,                 # Posición X (un poquito a la derecha de la barra)
                 bar.get_y() + bar.get_height()/2, # Posición Y (al centro de la barra)
                 f'{ancho:.1f}%',             # Texto a mostrar (1 decimal)
                 va='center', ha='left', fontsize=10)
    
    plt.tight_layout() # Ajusta los márgenes para que no se corte ningún texto
    plt.show()
def grafico_mapa(df_mejores): 
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

    Raises:
    ValueError:
        Si el DataFrame está vacío.
    """

    # Validar que existan resultados para mostrar
    if df_resultados.empty:
        raise ValueError( "No hay conciertos para representar en el mapa.")

    # Obtener las coordenadas del primer concierto
    # para centrar inicialmente el mapa
    latitud_centro = df_resultados.iloc[0]["latitud"]
    longitud_centro = df_resultados.iloc[0]["longitud"]

    # Crear el mapa base (crea objeto mapa)
    mapa = folium.Map(
        location=[latitud_centro, longitud_centro],
        zoom_start=11 )

    # Recorrer cada concierto del DataFrame, se pone el guión bajo para "ignorar" el índice
    for _, fila in df_resultados.iterrows():

        # Crear el texto que aparecerá al hacer clic
        texto_popup = (
            f"Artista: {fila['Artista/Banda']}<br>"
            f"Fecha: {fila['Fecha']}<br>"
            f"Precio: ${fila['Precio final']}<br>"
            f"Coincidencia: {fila['porcentaje_coincidencia']}%" )

        # Crear marcador para el concierto actual
        marcador = folium.Marker(
            location=[
                fila["latitud"],
                fila["longitud"]
            ],
            popup=texto_popup
        )

        # Agregar el marcador al mapa
        marcador.add_to(mapa)

    # Guardar el mapa en un archivo HTML
    mapa.save("mapa_conciertos.html")

    print(
        "Mapa generado correctamente: mapa_conciertos.html"
    )
