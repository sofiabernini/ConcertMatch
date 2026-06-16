# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 15:18:34 2026

@author: sofia
"""
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from src.cargar_dataset import carga_dataset
from src.filtrar_df import filtrar_df_bool, aplicar_filtros
from src.resultados import obtener_mejores, mostrar_info_resultados
from src.graficos import grafico_resultado
from src.pedir_preferencias import ordenar_preferencias, pedir_preferencias, hacer_pregunta_si_no
from src.calculo_coincidencias import ponderacion_total

# FUNCIÓN PRINCIPAL
def ejecutar_programa():
    """
    Ejecuta el programa. Termina mostrando los resultados e imprime un 
    mensaje que agradece por utilizar el programa.

    Returns
    -------
    None
    """
    # 1. Carga inicial del dataset
    ruta_archivo = 'data/concertmatch_dataset_prueba.csv'
    
    try: 
        df_original = carga_dataset(ruta_archivo) 
        print("Dataset cargado con éxito.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return 
    except (ValueError, PermissionError, RuntimeError) as e:
        print(f"Error al procesar los datos: {e}")
        return 

    # 2. Bucle principal de búsqueda
    while True:
        df = df_original.copy()
        
        # 3. Mensaje de Bienvenida
        print("="*50)
        print("🎸 BIENVENIDO A CONCERTMATCH V2 🎸")
        print("="*50)
        print("A continuación te haremos una serie de preguntas para determinar tus preferencias.")


# 4. Filtros previos obligatorios (Entradas y Movilidad)
        df = filtrar_df_bool(df,"Quedan entradas") 
        if df.empty:
            print("Lo sentimos, actualmente todos los eventos están agotados.")
            break #no hay nada que ofrecer, salimos del programa

        necesita_movilidad = hacer_pregunta_si_no("¿Necesitas acceso para personas con movilidad reducida? (si/no): ")
        if necesita_movilidad:
            df_temporal = filtrar_df_bool(df,"Acceso movilidad reducida")
            if not df_temporal.empty:
                df = df_temporal #actualizamos el DataFrame porque sí hay resultados
            else:
                print("Lo sentimos, no hay eventos disponibles con acceso para movilidad reducida.")
                continuar = hacer_pregunta_si_no("¿Deseas continuar buscando eventos sin este filtro? (si/no): ")
                if not continuar:
                    print("¡Gracias por usar ConcertMatch!")
                    break 

        # 5. Ordenar y Pedir Preferencias
        # Obtenemos la lista con el orden elegido por el usuario (ej: ["Género", "Lugar para sentarse", ...])
        categorias_ordenadas = ordenar_preferencias()
        
        # Obtenemos un diccionario con las respuestas exactas del usuario para cada categoría
        preferencias_usuario = pedir_preferencias(df, categorias_ordenadas)

        # 6. Filtrado y Cálculo de Coincidencias
        filtrado_preferencias= aplicar_filtros(df, preferencias_usuario, categorias_ordenadas)
        # Llamamos a la función ponderacion_total que creaste recién. 
        # Recibe el df filtrado y el diccionario de preferencias, y nos devuelve el df con los % finales.
        df_evaluado = ponderacion_total(df, preferencias_usuario)
        
        # 7. Mostrar resultados finales
        if not df_evaluado.empty:
            # Ahora usamos df_evaluado para obtener los mejores, ya que tiene la columna "porcentaje_coincidencia"
            mejores = obtener_mejores(df_evaluado) 
            
            grafico_resultado(mejores)
            mostrar_info_resultados(mejores)
        else:
            print("No quedaron eventos disponibles con esos filtros.")

        # 8. Reintentar
        print("-" * 50)
        reintentar = hacer_pregunta_si_no("¿Deseas realizar una nueva búsqueda? (si/no): ")
        
        if not reintentar:
            print("¡Gracias por usar ConcertMatch! Esperamos que disfrutes del evento.🎶")
            break 

if __name__ == "__main__":
    ejecutar_programa()
