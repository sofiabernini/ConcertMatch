# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 16:34:42 2026

@author: sofia
"""

# FUNCIÓN PARA OBTENER LOS 5 MEJORES RESULTADOS

def obtener_mejores(df, columna_porcentaje='porcentaje_coincidencia', top_n=5):
    """
    Ordena el DataFrame según el porcentaje de coincidencia de mayor a menor
    y devuelve los 'top_n' mejores resultados. (en este caso, el top 5)
    """
    if df.empty:
        return df
        
    # Ordenamos de mayor a menor coincidencia
    df_ordenado = df.sort_values(by=columna_porcentaje, ascending=False)
    
    # Devolvemos solo las primeras 'top_n' filas (por defecto 5)
    return df_ordenado.head(top_n)


# FUNCIÓN PARA MOSTRAR LA INFORMACIÓN EN CONSOLA

def mostrar_info_resultados(df_mejores):
    """
    Muestra en consola la información detallada de los resultados seleccionados.
    """
    if df_mejores.empty:
        return "Lo sentimos, actualmente no se encontraron eventos que coincidan con tus preferencias."


    print("="*50)
    print("⭐ TUS 5 MEJORES RECOMENDACIONES ⭐")
    print("="*50)
    
    for index, row in df_mejores.iterrows():
        print(f"🎵 Artista/Banda: {row['Artista/banda']} | Coincidencia: {row['porcentaje_coincidencia']}%")
        print(f"   - Género: {row['Género musical']}")
        print(f"   - Precio: ${row['Precio final']}")
        print(f"   - Fecha y Hora: {row['Fecha']} | {row['Horario']}")
        print(f"   - Lugar: {row['Estadio/Predio']} ({row['Ubicación']})")
        
        # Convertimos los booleanos en "Sí" o "No" para que sea más legible para el usuario 
        print(f"   - Movilidad Reducida: {'Sí' if row['Acceso movilidad reducida'] else 'No'}")
        print(f"   - Asientos: {'Sí' if row['Lugar para sentarse'] else 'No'}")
        print(f"   - Quedan entradas: {'Sí' if row['Quedan entradas'] else 'No'}")
        
        print(f"   - Lanzamiento entradas: {row['Lanzamiento venta']}")
        print(f"   - Link Entradas: {row['Link ticketera']}")



