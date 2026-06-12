#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:36:26 2026

@author: victoriamochnacs
"""
import pandas as pd
from geopy.geocoders import Nominatim

def validar_df (df):
    #validar columnas obligatorias
    #validar tipos de datos
    #validar valores lógicos
    
    validar_columnas(df)
    df_limpio = limpieza_df
    return df_limpio 
    
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
        "Ubicación",
        "Estadio/Predio",
        "Acceso movilidad reducida",
        "Lugar para sentarse",
        "Link ticketera",
        "Quedan entradas",
        "Lanzamiento venta"
    ]
    
    faltantes = []
    
    for columna in COLUMNAS_OBLIGATORIAS:
        if columna not in df.columns:
            faltantes.append(columna)
    
    if faltantes: 
        raise ValueError (f"Faltan columnas esenciales: {faltantes}. Función: validar_columnas en validar_df.py")
        
    return True

#Validar tipos de datos
def limpieza_df(df):
#validar que el df no esté vacío

    if df.empty:
        raise ValueError ("Error: El Dataframe está vacío. Función: validar_datos en validar_df.py")
        
        
    columnas_criticas = [
        "Artista/Banda",
        "Género musical",
        "Precio final",
        "Fecha",
        "Horario",
        "Ubicación"
        "Acceso movilidad reducida"
        "Lugar para sentarse"
        "Quedan entradas"
        "Lanzamiento venta"
    ]
    
#validar cada tipo de dato

#artista y género no hace falta validarlos, solo que no sean vacíos

#precio final:         
    df["Precio final"] = pd.to_numeric(
       df["Precio final"],
       errors = "coerce")

    df.loc[df["Precio final"]< 0,
           "Precio final"] = pd.NA
     
        
#Validación de fechas
#Columna "fecha":
    df["Fecha"] = pd.to_datetime(
        df["Fecha"], 
        errors = "coerce"
        )
    
#Columna "Lanzamiento venta"
    df["Lanzamiento venta"] = pd.to_datetime(
        df["Lanzamiento venta"],
        errors = "coerce"
        )

#Validación de horarios
    df["Horario"] = pd.to_datetime(
        df["Horario"], 
        format="%H:%M",
        errors="coerce").dt.time

#Validación booleanos (Acceso movilidad reducida, Lugar para sentarse, Quedan entradas)

    valores_validos = {True, False}
    
    df.loc[
        ~df["Quedan entradas"].isin(valores_validos),
        "Quedan entradas"] = pd.NA
    
    df.loc[
        ~df["Acceso movilidad reducida"].isin(valores_validos),
        "Acceso movilidad reducida"] = pd.NA
    
    df.loc[
        ~df["Lugar para sentarse"].isin(valores_validos),
        "Lugar para sentarse"] = pd.NA
    
#Link ticketera. En este caso, no validé. 
#Sino que, simplemente, los valores NaN van a mostrarse 
#como un mensaje "curado" para el usuario. El link no es una 
#información tan crucial. Capaz no hay un link de venta de entradas como tal
#(como en el caso de un festival de la ciudad)

    if df["Link"].isnull().any():
        df["Link"]= df["Link"].fillna("Este evento no tiene un link a la compra de entradas. Recomendamos buscar más información en páginas oficiales del evento, así como en redes sociales")
      
    
#Validación de Ubicación
    geolocator = Nominatim (user_agent = "concertmatch")
    
    for i in df.index:
        
        direccion = df.loc[i, "Ubicación"]
        
        try:
            resultado = geolocator.geocode(direccion)
        except Exception:
            resultado = None

        if resultado is None:
            df.loc[i, "Ubicación"] = pd.NA

#eliminar datos tipo Nan con dropna()
    df_limpio = df.dropna(subset = columnas_criticas)

    return df_limpio










