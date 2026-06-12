#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 19:13:18 2026

@author: victoriamochnacs
"""

import pandas as pd
import os
from src.validar_df import validar_df #solo importo la de validar_df porque contiene a validar_columnas() y limpieza_df()

def carga_dataset(ruta_archivo):
    """
    Toma una ruta de archivo CSV, lo abre y lo convierte a un DataFrame de pandas.

    Realiza validaciones para asegurar que el archivo existe, se puede leer
    y contiene datos.

    Parámetros:
    -----------
    ruta_archivo : str
        La ruta donde se encuentra el archivo CSV.

    Retorna:
    --------
    pd.DataFrame
        El DataFrame con los datos cargados del archivo.

    Excepciones (Raises):
    -------------------
    FileNotFoundError:
        Si la ruta especificada no existe o el archivo no se encuentra.
    ValueError:
        Si el archivo está completamente vacío, si solo contiene encabezados 
        pero no datos, o si el formato está corrupto/es inválido.
    PermissionError:
        Si el programa no tiene permisos del sistema operativo para abrir el archivo.
    RuntimeError:
        Si ocurre cualquier otro error inesperado durante la lectura.
    """
    
    # 1. Verificar si la ruta o el archivo realmente existen
    if not os.path.exists(ruta_archivo):
        raise FileNotFoundError(f"El archivo no existe en la ruta especificada: '{ruta_archivo}'")
    
    # 2. Intentar cargar el archivo y capturar errores específicos de pandas/sistema
    try:
        # Se asume formato CSV por defecto. 
        df = pd.read_csv(ruta_archivo)
        
    except pd.errors.EmptyDataError:
        # Este error salta si el archivo tiene 0 bytes
        raise ValueError(f"El archivo '{ruta_archivo}' está completamente vacío.")
        
    except pd.errors.ParserError:
        # Este error salta si el archivo está mal estructurado (ej. columnas disparejas)
        raise ValueError(f"El archivo '{ruta_archivo}' no tiene un formato tabular válido o está corrupto.")
        
    except PermissionError:
        # Este error salta si el archivo está bloqueado por otro programa o no hay permisos
        raise PermissionError(f"No hay permisos suficientes para leer el archivo '{ruta_archivo}'.")
        
    except Exception as e:
        # Captura de seguridad para cualquier otro error imprevisto
        raise RuntimeError(f"Ocurrió un error inesperado al leer el archivo: {e}")
    
    # 3. Verificar si el DataFrame se creó, pero no tiene datos (ej. solo tiene la fila de títulos)
    if df.empty:
        raise ValueError(f"El archivo '{ruta_archivo}' se leyó correctamente, pero el dataset no contiene eventos (está vacío).")
    
    try: 
        df = validar_df(df)
    except ValueError as e:
        raise ValueError (e)
    
    return df


    
