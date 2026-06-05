# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 19:21:51 2026

@author: sofia
"""

def filtrar_df_bool(df, columna):
    """
    Analiza el DataFrame y elimina las filas que tengan el valor False 
    en la columna especificada por parámetro.
    
    Parámetros:
    - df (DataFrame): El dataset a evaluar.
    - columna (str): El nombre exacto de la columna a verificar.
    
    Retorna:
    - DataFrame: El dataset actualizado solo con las filas que son True.
    """
    # Conservamos solo las filas donde el valor de la columna sea True
    df_actualizado = df[df[columna] == True]
    
    return df_actualizado