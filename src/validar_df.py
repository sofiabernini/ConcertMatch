#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:36:26 2026

@author: victoriamochnacs
"""
import pandas as pd
from geopy.geocoders import Nominatim

def validar_df (df):
    '''
    Descipción: Es una función que llama a otras funciones, para validar 
    las columnas y los tipo de datos del dataframe.

    Parameters
    ----------
    df : dataframe.

    Returns
    -------
    df_limpio : dataframe con los datos validados y limpios para poder ejecutar el resto del programa
    

    '''
    #validar columnas obligatorias
    #validar tipos de datos
    #validar valores lógicos
    
    validar_columnas(df)
    df_limpio = limpieza_df(df)
    return df_limpio 
    
def validar_columnas (df):
    '''
    Descripción: Esta función valida que el dataframe tenga las columnas necesarias para ejecutar el programa

    Parameters
    ----------
    df : Dataframe de pandas.

    Returns
    -------
    True 
    
    Raises
    -------
    ValueError: si faltan columnas esenciales para el correcto funcionamiento del programa.
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

#Validar tipos de datos: llama a todas las funciones anteriores
def limpieza_df(df):
    '''
    Descripción: Es una función que coordina otras funciones de limpieza de los tipos de datos del dataframe. 
    Elimina del df todas las filas con datos tipo NaN (si es que esos datos están en alguna de las columnas_críticas) 

    Parameters
    ----------
    df : DataFrame.

    Returns
    -------
    df_limpio: Dataframe (luego de pasar por la limpieza de datos).
    
    Raises
    -------
    ValueError: si el df está vacío

    '''
    
#validar que el df no esté vacío
    if df.empty:
        raise ValueError ("Error: El Dataframe está vacío. Función: validar_datos en validar_df.py")
        
#Se define una lista con las columnas que, si cuentan con datos incorrectos, podrían crear problemas en la ejecución del programa    
    columnas_criticas = [
        "Artista/Banda",
        "Género musical",
        "Precio final",
        "Fecha",
        "Horario",
        "Ubicación",
        "Acceso movilidad reducida",
        "Lugar para sentarse",
        "Quedan entradas",
        "Lanzamiento venta"
    ]


#llamado a funciones que convierten los datos inválidos a Nan  
    df = limpiar_precios(df)
    df = limpiar_fechas (df)
    df = limpiar_horario (df)
    df = limpiar_booleanos (df)
    df = manejar_links_vacios(df)
    df = limpiar_ubicacion(df)
    
#eliminar datos tipo Nan con dropna()

    df_limpio = df.dropna(subset = columnas_criticas)

    
    return df_limpio



def limpiar_precios (df):
    '''
    Descripción: Esta función convierte los valores de la columna de "Precio final" del dataframe
    a Nan si no se pueden convertir a número o si es un valor menor a 0
    

    Parameters
    ----------
    df : DataFrame.

    Returns
    -------
    df : DataFrame (con la conversión de los datos).

    '''
    df["Precio final"] = pd.to_numeric (df["Precio final"], errors = "coerce")
    df.loc[df["Precio final"]< 0, "Precio final"] = pd.NA
    return df

def limpiar_fechas (df):
    '''
    Descripción: Esta función convierte los valores de las columnas de "Fecha" y "Lanzamiento venta" a
    formato fecha, y si no puede realizar la conversion, trasforma ese dato a Nan

    Parameters
    ----------
    df : DataFrame.

    Returns
    -------
    df : DataFrame (con la conversión de datos).

    '''
    df["Fecha"] = pd.to_datetime (df["Fecha"], errors = "coerce")
    df["Lanzamiento venta"] = pd.to_datetime (df["Lanzamiento venta"], errors = "coerce")
    return df
    
def limpiar_horario (df):
    '''
    Descripción: Esta función convierte los valores de la columna de "Horario" al formato correspondiente. 
    Si no puede realizar la conversión, se transforma el dato a Nan

    Parameters
    ----------
    df : DataFrame.

    Returns
    -------
    df : DataFrame (con la conversión de datos).

    Raises: No hay (solo convierte a Nan)
    '''
    
    df["Horario"] = pd.to_datetime (df["Horario"], format= "%H:%M", errors = "coerce").dt.time
    return df

    

def limpiar_booleanos(df):
    '''
    Descripción: Esta función revisa que las columnas de "Quedan entradas", 
    "Acceso movilidad reducida" y "Lugar para sentarse" cuenten con datos booleanos True o False. 
    Si alguno de los datos no cumple esta condicion se lo transforma a Nan
    
    Parameters
    ----------
    df : DataFrame.
    
    Returns
    -------
    df : DataFrame (con la conversión de datos).
   
    Raises: No hay (solo convierte a Nan)

    '''
    valores_validos = [True, False]
    
    for columna in ["Quedan entradas", "Acceso movilidad reducida", "Lugar para sentarse"]:
        df[columna] = df[columna].map({"True": True, "False": False, True: True, False: False})
        #se usa este map y los valores que no coincidan se transforman a Nan automáticamente
    
    return df

def manejar_links_vacios(df):
    '''
    Descripción: Esta función genera un mensaje específico para las celdas en las columnas de 
    "Link ticketera" que tengan un valor Nan 

    Parameters
    ----------
    df : DataFrame.

    Returns
    -------
    df : DataFrame (con la conversión de datos).

    '''
    
    if df["Link ticketera"].isnull().any():
        df["Link ticketera"]= df["Link ticketera"].fillna(
            "Este evento no tiene un link a la compra de entradas." 
            "Recomendamos buscar más información en páginas oficiales del evento, así como en redes sociales")
    
    return df
    
def limpiar_ubicacion (df):
    '''
    Descripción: Esta función valida que las direcciones de la columna "Ubicación" existan, 
    utilizando métodos de la librería "Geopy"

    Parameters
    ----------
    df : DataFrame.

    Returns
    -------
    df : DataFrame (con la conversión de los datos).

    '''
    
    geolocator = Nominatim (user_agent = "concertmatch")
    
    for i in df.index:
        
        direccion = df.loc[i, "Ubicación"]
        
        try:
            resultado = geolocator.geocode(direccion)
            time.sleep(1)
        except Exception:
            resultado = None

        if resultado is None:
            df.loc[i, "Ubicación"] = pd.NA
            
    return df
    
    












