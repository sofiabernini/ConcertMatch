# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 15:18:34 2026

@author: sofia
"""

#PROGRAMA PRINCIPAL:
    
#Primero transformamos el DataSet en un DataFrame de Python

import pandas as pd

# Leer el dataset que está dentro de la carpeta 'datos'
# encoding='utf-8' --> hace que los nombres con acentos o eñes no generen un error de decodificación
df = pd.read_csv('datos/concertmatch_dataset_prueba.csv', encoding='utf-8')

# Ver las primeras 5 filas para comprobar que se cargó correctamente
print(df.head()) #esto se borra después, era para probar nomás

