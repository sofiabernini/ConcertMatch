#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 20:20:33 2026

@author: victoriamochnacs
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


## "La función aplicar_filtros() recorre las categorías según el orden elegido por el usuario y delega el filtrado a filtrar_por_condicion(), que selecciona automáticamente el criterio (que funcion de filtrado usar) adecuado según el tipo de dato."

from datetime import datetime


def filtrar_por_condicion(df, categoria, condicion):
    """
    Descripción: Filtra el DataFrame según la categoría y la condición
    recibidas.

    Parámetros:
        df (DataFrame) - dataset a filtrar.
        categoria (str) - categoría por la cual se desea filtrar.
        condicion - valor utilizado para realizar el filtro.

    Retorno:
        DataFrame - dataset filtrado.

    Manejo de errores:
        - Se asume que las preferencias ya fueron validadas en las
          funciones que las solicitaron al usuario.
    """

    ## Categorías que reciben una lista de valores
    if categoria in [
        "Género musical",
        "horario",
        "ubicación"
    ]:

        return df[df[categoria].isin(condicion)]

    ## Precio máximo aceptado
    elif categoria == "precio final":

        return df[df[categoria] <= condicion]

    ## Rango de fechas
    elif categoria == "fecha":

        fecha_1 = condicion["fecha_1"]
        fecha_2 = condicion["fecha_2"]

        return df[
            (df[categoria] >= fecha_1)
            &
            (df[categoria] <= fecha_2)
        ]

    ## Valores booleanos
    elif categoria in [
        "Acceso para movilidad reducida",
        "Cuenta con asientos"
    ]:

        return df[df[categoria] == condicion]

