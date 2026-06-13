# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 15:18:34 2026

@author: sofia
"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from src.cargar_dataset import carga_dataset, validar_dataframe
from src.filtrar_df import filtrar_df_bool
from src.resultados import obtener_mejores, mostrar_info_resultados
from src.graficos import grafico_resultado
from src.pedir_preferencias import ordenar_preferencias


def hacer_pregunta_si_no(mensaje):
    """
    Se encarga de hacer una pregunta de si/no al usuario.
    Maneja los errores internamente y devuelve True (sí) o False (no).

    Parameters
    ----------
    mensaje : str
        Pregunta que se reponde con sí o no.

    Returns
    -------
    bool
        Devuelve True si el usuario respondió que sí o False si el usuario respondió que no.

    """
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta == "si":
            return True
        elif respuesta == "no":
            return False
        else:
            print("Opción no válida. Por favor, escribe 'si' o 'no'.")



# FUNCIÓN PRINCIPAL

def ejecutar_programa():
    """
    Ejecuta el programa. Termina mostrando los resultados e imprime un mensaje que agradece por utilizar el programa.

    Returns
    -------
    None
        

    """
    # 1. Carga inicial del dataset (Se hace UNA sola vez al principio)
    ruta_archivo = 'datos/concertmatch_dataset_prueba.csv'
    
    try: 
        df_original = carga_dataset(ruta_archivo) 
        print("Dataset cargado con éxito.")
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return # Termina el programa porque sin datos no se puede seguir
        
    except (ValueError, PermissionError, RuntimeError) as e:
        print(f"Error al procesar los datos: {e}")
        return # Termina el programa

    # 2. Bucle principal de búsqueda (Permite hacer múltiples búsquedas sin recargar el archivo)
    while True:
        # Usamos una copia del DataFrame para no arruinar el original en cada búsqueda
        df = df_original.copy()
        
        # 3. Mensaje de Bienvenida
        print("="*50)
        print("🎸 BIENVENIDO A CONCERTMATCH V2 🎸")
        print("="*50)
        print("A continuación te haremos una serie de preguntas para determinar tus preferencias y así recomendarte eventos disponibles que coincidan con tus gustos.")

        # 4. Primer Filtro/Pregunta: Entradas Disponibles
        df = filtrar_df_bool(df, True, "quedan entradas") 
        
        if df.empty:
            print("Lo sentimos, actualmente todos los eventos están agotados.")
            break # No hay nada que ofrecer, salimos del programa.

        # 5. Segundo Filtro/Pregunta: Movilidad reducida
        necesita_movilidad = hacer_pregunta_si_no("¿Necesitas acceso para personas con movilidad reducida? (si/no): ")
        
        if necesita_movilidad:
            df_temporal = filtrar_df_bool(df, True, "Acceso movilidad reducida")
            
            if not df_temporal.empty:
                df = df_temporal # Actualizamos el DataFrame porque hay resultados
            else:
                print("Lo sentimos, actualmente no hay eventos disponibles con acceso para movilidad reducida.")
                continuar = hacer_pregunta_si_no("¿Deseas continuar buscando eventos sin este filtro? (si/no): ")
                
                if not continuar:
                    print("¡Gracias por usar ConcertMatch!")
                    break # Rompe el bucle principal y termina el programa

        # 6. Tercer Filtro/Pregunta: Lugar para sentarse
        quiere_asientos = hacer_pregunta_si_no("¿Deseas que el lugar cuente con asientos? (si/no): ")
        
        if quiere_asientos:
            df_temporal = filtrar_df_bool(df, True, "Lugar para sentarse")
            if not df_temporal.empty:
                df = df_temporal
            else:
                print("No hay eventos con asientos que cumplan tus filtros anteriores. Continuaremos sin este filtro.")

        # Acá falta el resto de los filtros y el cálculo de coincidencias
        # df_evaluado = calcular_porcentajes(df, preferencias...)

        # 7. Mostrar resultados finales
        if not df.empty:
            # (Cambiar 'df' por 'df_evaluado' una vez que se agregaron los porcentajes de coincidencia)
            # Reordena filas del dataframe de mayor a menor porcentaje de coincidencia y devuelve los 5 mejores
            mejores = obtener_mejores(df) 
            
            # Son 2 formas de mostrar los resultados (falta una más)
            grafico_resultado(mejores)
            mostrar_info_resultados(mejores)
        else:
            print("No quedaron eventos disponibles con esos filtros.")

        # 8. Preguntar si desea volver a ejecutar
        print("-" * 50)
        reintentar = hacer_pregunta_si_no("¿Deseas realizar una nueva búsqueda? (si/no): ")
        
        if not reintentar:
            print("¡Gracias por usar ConcertMatch! Esperamos que disfrutes del evento.🎶")
            break # Rompe el bucle principal y el programa termina de ejecutarse


#PROGRAMA PRINCIPAL
lista_categorias_ordenadas= ordenar_preferencias() 
inicio_fin = ejecutar_programa()




