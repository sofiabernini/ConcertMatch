# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 16:34:42 2026

@author: sofia
"""

# 1. FUNCIÓN PARA MOSTRAR LA INFORMACIÓN EN CONSOLA

def mostrar_info_resultados(df_mejores):
    """
    Muestra en consola la información detallada de los resultados seleccionados.
    """
    if df_mejores.empty:
        print("Lo sentimos, actualmente no se encontraron eventos que coincidan con tus preferencias.)
        return

    print("\n" + "="*50)
    print("⭐ TUS 5 MEJORES RECOMENDACIONES ⭐")
    print("="*50)
    
    for index, row in df_mejores.iterrows():
        print(f"🎵 Artista/Banda: {row['artista_banda']} | Coincidencia: {row['porcentaje_coincidencia']}%")
        print(f"   - Género: {row['genero']}")
        print(f"   - Precio: ${row['precio']}")
        print(f"   - Fecha y Hora: {row['fecha']} | {row['hora']}")
        print(f"   - Lugar: {row['lugar']} ({row['direccion']})")
        
        # Convertimos los booleanos en "Sí" o "No" para que sea más legible para el usuario 
        print(f"   - Movilidad Reducida: {'Sí' if row['acceso_movilidad_reducida'] else 'No'}")
        print(f"   - Asientos: {'Sí' if row['cuenta_con_asientos'] else 'No'}")
        print(f"   - Quedan entradas: {'Sí' if row['quedan_entradas'] else 'No'}")
        
        print(f"   - Lanzamiento entradas: {row['lanzamiento_entradas']}")
        print(f"   - Link Entradas: {row['ticketera_link']}")



# 2. FUNCIÓN PARA MOSTRAR EL GRÁFICO

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