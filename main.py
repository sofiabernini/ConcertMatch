# -*- coding: utf-8 -*-

print ("================ 🎵 CONCERTMATCH 🎵 ==================")
print("Comenzando proceso de carga del programa. Podría tardarse unos segundos/minutos, dependiendo de la cantidad de conciertos cargados")
print("Espere a que aparezca el cartel de bienvenida del programa")

## ========= Import de módulos y funciones ===============
from src.cargar_dataset import carga_dataset
from src.filtrar_df import filtrar_df_bool, aplicar_filtros
from src.resultados import (obtener_columna_importante,ordenar_resultados,mostrar_info_resultados)
from src.graficos import crear_histograma_comparativo, grafico_mapa
from src.pedir_preferencias import (ordenar_preferencias,pedir_preferencias,hacer_pregunta_si_no)


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
        FileNotFoundError: Si no se pudo encontrar la ruta de archivo
        ValueError: Error de procesamiento de datos
        PermissionError: Error de procesamiento de datos
        RuntimeError: Error de procesamiento de datos
        
        Si el programa presenta alguno de estos errores, se corta la ejecución y se muestra el mensaje
    """

## ===== Carga inicial del dataset ==============
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


##======== Bucle principal de búsqueda =======================

    #Permite realizar varias búsquedas sin volver a cargar el archivo.
    while True:

        df = df_original.copy()

        print("=" * 50)
        print("🎸 BIENVENIDO A CONCERTMATCH 🎸")
        print("=" * 50)

        print("A continuación te haremos una serie de preguntas para determinar tus preferencias.")


        ## Filtros previos necesarios (Entradas y movilidad)
        # 1. Se eliminan los conciertos sin entradas disponibles.
        df = filtrar_df_bool(df, "Quedan entradas")

        if df.empty:
            print("Actualmente todos los conciertos se encuentran agotados.")
            #Si el df está vacío, se corta la ejecución del programa
            break


        ## 2. Se pregunta por Acceso a movilidad reducida.
        necesita_movilidad = hacer_pregunta_si_no("¿Necesitás acceso para personas con movilidad reducida? (si/no): ")

        if necesita_movilidad:
            df_temporal = filtrar_df_bool(df,"Acceso movilidad reducida")

            if not df_temporal.empty:
                df = df_temporal

            else:
                print("No existen conciertos con acceso para personas con movilidad reducida.")
                
                #Se le da la posibilidad al usuario de continuar sin el requerimiento del Acceso a movilidad reducida
                # si es que no hay conciertos que cumplan esa condición)
                continuar = hacer_pregunta_si_no("¿Deseás continuar sin este requisito? (si/no): ")
                
                if not continuar:
                    print("¡Gracias por utilizar ConcertMatch!")
                    break

## ========= Orden y definición de preferencias del usuario ==============


        ## Se obtiene el orden de preferencias definido.
        categorias_ordenadas = ordenar_preferencias()


        ## Se solicitan las preferencias del usuario para las categorías:
            # Género
            # Precio
            # Distancia máxima (incluye pregunta de ubicación de partida.
            # Franja horaria
            # Fecha o rango de fechas
            # Disponibilidad de asientos
        ## Las respuestas se guardan en un diccionario
        ## Además devuelve el DataFrame con la columna
        ## "distancias" ya calculada respecto a la ubicación del usuario.
        
        preferencias_usuario, df = pedir_preferencias(df, categorias_ordenadas)


        ## Se aplican los filtros según el diccionario de preferencias.
        df_filtrado = aplicar_filtros(df, preferencias_usuario, categorias_ordenadas)

        ## Se determina si la prioridad principal es
        ## precio o distancia
        columna_importante = obtener_columna_importante(categorias_ordenadas)

        ## Se ordenan los conciertos.
        df_ordenado = ordenar_resultados(df_filtrado, columna_importante)


## ========= Gráficos y resumenes de información ================

        ## Se genera el histograma.
        crear_histograma_comparativo(df_original, df_ordenado, columna_importante)

        ## Se muestran los primeros cinco conciertos.
        mostrar_info_resultados(df_ordenado)
        
        ## Se genera el mapa con la información de los conciertos
        grafico_mapa(df_ordenado)


## ========== Volver a ingresar conciertos ¿Si o no? ===========
        print("-" * 50)

        reintentar = hacer_pregunta_si_no("¿Deseás realizar otra búsqueda? (si/no): ")

        if not reintentar:
            print("¡Gracias por usar ConcertMatch! Esperamos que disfrutes del evento. 🎶")
            break


if __name__ == "__main__":

    ejecutar_programa()   

