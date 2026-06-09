# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 16:46:50 2026

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