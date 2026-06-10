#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 20:28:55 2026

@author: victoriamochnacs
"""

# FUNCIÓN PARA MOSTRAR EL GRÁFICO CON LOS PORCENTAJES DE COINCIDENCIA

def grafico_resultado(df_mejores):
    """
    Muestra un gráfico de barras horizontales con los mejores resultados.
    """
    if df_mejores.empty:
        return
        
    plt.figure(figsize=(10, 6))
    
    # Creamos el gráfico de barras horizontales
    bars = plt.barh(df_mejores['artista_banda'], df_mejores['porcentaje_coincidencia'], color='mediumpurple')
    
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