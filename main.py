# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 15:18:34 2026

@author: sofia
"""

from src.cargar_dataset import carga_dataset
from src.filtrar_df import filtrar_df_bool, aplicar_filtros
from src.resultados import (obtener_columna_importante,ordenar_resultados,mostrar_info_resultados)
from src.graficos import crear_histograma_comparativo, grafico_mapa
from src.pedir_preferencias import (ordenar_preferencias,pedir_preferencias,hacer_pregunta_si_no)


#FUNCIÓN PRINCIPAL:
def ejecutar_programa():
    """
    Descripción:
        Ejecuta el programa completo.

        Carga el dataset, solicita las preferencias del usuario,
        aplica los filtros correspondientes, ordena los conciertos
        según la categoría más importante entre precio y distancia,
        genera un histograma y muestra los conciertos recomendados.

    Returns:
        None

    Manejo de errores:
        - Si ocurre un error al cargar el dataset, el programa lo informa y luego finaliza.
    """

    # Carga inicial del dataset.
    ruta_archivo = "data/concertmatch_dataset_prueba.csv"

    try:
        df_original = carga_dataset(ruta_archivo)
        print("Dataset cargado con éxito.")

    except FileNotFoundError as e:
        print(f"Error: {e}")
        return

    except (ValueError, PermissionError, RuntimeError) as e:
        print(f"Error al procesar los datos: {e}")
        return

    # Permite realizar varias búsquedas sin volver a cargar el archivo o ejecutar todo el programa denuevo
    while True:

        df = df_original.copy()

        print("=" * 50)
        print("🎸 BIENVENIDO A CONCERTMATCH 🎸")
        print("=" * 50)

        print("A continuación te haremos una serie de preguntas para determinar tus preferencias.")

        # Se eliminan los conciertos sin entradas disponibles.
        df = filtrar_df_bool(df,"Quedan entradas") 

        if df.empty:
            print("Lo sentimos, actualmente todos los conciertos se encuentran agotados.")
            break # No hay nada que ofrecer, salimos del programa

        # Filtro obligatorio para movilidad reducida.
        necesita_movilidad = hacer_pregunta_si_no("¿Necesitas acceso para personas con movilidad reducida? (si/no): ")
       
        if necesita_movilidad:
            df_temporal = filtrar_df_bool(df,"Acceso movilidad reducida")
            if not df_temporal.empty:
                df = df_temporal # Actualizamos el DataFrame porque sí hay resultados que coinciden con la preferencia
            else:
                print("Lo sentimos, no hay eventos disponibles con acceso para movilidad reducida.")
                continuar = hacer_pregunta_si_no("¿Deseas continuar buscando eventos sin este filtro? (si/no): ")
                if not continuar:
                    print("¡Gracias por usar ConcertMatch!")
                    break 

        # Se obtiene el orden de importancia elegido.
        categorias_ordenadas = ordenar_preferencias()

        # Se solicitan las preferencias del usuario.
        # Además devuelve el DataFrame con la columna "distancias" ya calculada.
        preferencias_usuario, df = pedir_preferencias(df,categorias_ordenadas)

        # Se aplican los filtros.
        df_filtrado = aplicar_filtros(df,preferencias_usuario,categorias_ordenadas)

        # Se determina si la prioridad principal es precio o distancia.
        columna_importante = obtener_columna_importante(categorias_ordenadas)

        # Se ordenan los conciertos.
        df_ordenado = ordenar_resultados(df_filtrado,columna_importante)

        # Se genera el histograma.
        crear_histograma_comparativo(df_original,df_ordenado,columna_importante)

        # Se genera el mapa con la información de los conciertos
        grafico_mapa(df_ordenado)
        
        # Se muestran los primeros cinco conciertos que más coinciden con las preferencias del usuario.
        mostrar_info_resultados(df_ordenado)

        print("-" * 50)

        reintentar = hacer_pregunta_si_no("¿Deseás realizar otra búsqueda? (si/no): ")

        if not reintentar:
            print("¡Gracias por usar ConcertMatch! Esperamos que disfrutes del evento. 🎶")
            break

#PROGRAMA PRINCIPAL:
print("Comenzando proceso de carga del programa. Podría tardarse unos segundos/minutos")
print("Espere a que aparezca el cartel de inicio del programa")

if __name__ == "__main__":
    ejecutar_programa()