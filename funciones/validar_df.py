#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:36:26 2026

@author: victoriamochnacs
"""

def validar_dataframe (df):
    #validar columnas obligatorias
    #validar tipos de datos
    #validar valores lógicos
    columnas = validar_columnas (df)
    datos = validar_datos(df)
    
def validar_columnas (df):
    '''
    descripción: es una función que valida que el dataframe tenga las columnas necesarias para ejecutar el programa

    Parameters
    ----------
    df : TYPE
        DESCRIPTION.

    Returns
    -------
    None.
    '''
    
#VALIDAR COLUMNAS
    COLUMNAS_OBLIGATORIAS = [
        "Artista/Banda",
        "Género musical",
        "Precio final",
        "Fecha",
        "Horario",
        "Ubicación"
        "Estadio/Predio"
        "Acceso movilidad reducida"
        "Lugar para sentarse"
        "Link ticketera"
        "Quedan entradas"
        "Lanzamiento venta"
    ]
    
    faltantes = []
    
    for columna in COLUMNAS_OBLIGATORIAS:
        if columna not in df.columns:
            faltantes.append(columna)
    
    if faltantes: 
        raise ValueError (f"Faltan las columnas: {faltantes}")
        
    return True

#Validar tipos de datos
def validar_datos (df):
    if        




