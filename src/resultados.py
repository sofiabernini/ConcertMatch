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
        print("Lo sentimos, actualmente no se encontraron eventos que coincidan con tus preferencias.)
        return

    print("="*50)
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



