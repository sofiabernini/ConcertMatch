# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 15:18:34 2026

@author: sofia
"""

#PROGRAMA PRINCIPAL:
    
#Primero transformamos el DataSet en un DataFrame de Python

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Leer el dataset que está dentro de la carpeta 'datos'
# encoding='utf-8' --> hace que los nombres con acentos o eñes no generen un error de decodificación
try:
    df = pd.read_csv('datos/concertmatch_dataset_prueba.csv', encoding='utf-8')
except FileNotFoundError:
    print("Error: El DataFrame no fue encontrado.")
    
except Exception as e:
    print(f"Ocurrió un error inesperado al cargar la base de datos: {e}")

#Actualiza el DataFrame dejando solo los eventos con entradas disponibles
df = filtrar_df_bool(df, "quedan entradas")
#Faltaría controlar el caso de que quede vacío el DataFrame porque todos los eventos estaban agotados.

#Mensaje de Bienvenida:
print("\n" + "="*50)
print("🎸 BIENVENIDO A CONCERTMATCH V2 🎸")
print("="*50)
print("A continuación te haremos una serie de preguntas para determinar tus preferencias y así recomendarte 5 eventos disponibles que coinciden con tus gustos.")

#Pregunta si necesita acceso para personas con movilidad reducida:
while True:
    movilidad = input("¿Necesitas acceso para personas con movilidad reducida? (si/no): ").strip().lower()
    if movilidad == "si":
        df_requiere_movilidad = filtrar_df_bool(df, "Acceso movilidad reducida")
        if not df_requiere_movildad.empty:
            df = df_requiere_movilidad
            break
        else:
            print("Lo sentimos, actualmente no hay eventos disponibles con acceso para movilidad reducida.")
            while True:
                continuar = input("¿Deseas continuar buscando eventos sin este filtro? (si/no): ").strip().lower()
                if continuar == "si":
                    break 
                elif continuar == "no":
                    print("¡Gracias por usar ConcertMatch!")
                    break
                else:
                    print("Opción no válida. Escriba 'si' o 'no'.")
    
    elif movilidad == "no":
        break
        
    else:
        print("Opción no válida. Escriba 'si' o 'no'.")
    
# Esta línea de código es para cuanto haya que filtrar el df para que se quede solo con los evento que SÍ tienen asientos.
df = filtrar_verdaderos(df, "Lugar para sentarse")
        
        
#Esto va al final de todo el programa, después de mostrar los resultados/graáficos:
#Pregunta si desea volver a ejecutar el programa:
while True:
    reintentar = input("¿Deseas realizar una nueva búsqueda? (si/no): ").strip().lower()
    if reintentar == "si":
        #¿Llamar a la función "ejecutar_programa"?
        
    elif reintentar == "no":
        print("¡Gracias por usar ConcertMatch! Esperamos que disfrutes del evento. 🎶")
        break
    
    else:
        print("Opción no válida. Escriba 'si' o 'no'.")