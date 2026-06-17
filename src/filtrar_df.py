#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 20:20:33 2026

@author: victoriamochnacs
"""
from src.pedir_preferencias import pedir_nueva_preferencia

def filtrar_df_bool(df, columna):
    """
    Descripción: Analiza el DataFrame y elimina las filas que tengan el valor False 
    en la columna especificada por parámetro.
    
    Parámetros:
    - df (DataFrame): El dataset a evaluar.
    - columna (str): El nombre exacto de la columna a verificar.
    
    Retorna:
    - df_actualizado: El DataFrame actualizado solo con las filas que son True para la condición booleana pedida.
    """
    # Conservamos solo las filas donde el valor de la columna sea True
    df_actualizado = df[df[columna] == True]
    
    return df_actualizado


def filtrar_rango(df, columna, minimo, maximo):
    """
    Descripción:
        Filtra un DataFrame utilizando un rango mínimo y máximo.

    Parámetros:
        df (DataFrame) - dataset a filtrar.
        columna (str) - nombre de la columna.
        minimo - valor mínimo permitido.
        maximo - valor máximo permitido.

    Retorno:
        DataFrame filtrado.

    Manejo de errores:
        No realiza validaciones porque los datos ya fueron
        validados en las funciones que solicitan las preferencias.
    """

    return df[
        (df[columna] >= minimo)
        &
        (df[columna] <= maximo)
    ]

def filtrar_por_condicion(df, categoria, condicion):
    """
    Descripción:
        Aplica el filtro correspondiente según la categoría
        seleccionada por el usuario.

    Parámetros:
        df (DataFrame) - dataset a filtrar.
        categoria (str) - categoría utilizada para filtrar.
        condicion - preferencia asociada a la categoría.

    Retorno:
        DataFrame - dataset filtrado.

    Manejo de errores:
        No realiza validaciones porque las preferencias ya fueron
        verificadas por las funciones que las solicitan.
    """

    ## Géneros seleccionados por el usuario.
    if categoria == "genero":

        return df[
            df["Género musical"].isin(condicion)
        ]

    ## Rango de precios.
    elif categoria == "precio":

        return filtrar_rango(
            df,
            "Precio final",
            condicion["min"],
            condicion["max"]
        )

    ## Rango de fechas.
    elif categoria == "fecha":

        return filtrar_rango(
            df,
            "Fecha",
            condicion["fecha_1"],
            condicion["fecha_2"]
        )

    ## Rango horario.
    elif categoria == "horario":

        return filtrar_rango(
            df,
            "Horario",
            condicion["hora_1"],
            condicion["hora_2"]
        )

    ## Distancia máxima.
    elif categoria == "distancia":

        return df[
            df["distancia"] <= condicion
        ]

    ## Necesita asientos.
    elif categoria == "lugar para sentarse":

        return df[
            df["Lugar para sentarse"] == condicion
        ]
    
def aplicar_filtros(df_filtrado,
                    dic_preferencias,
                    categorias_ordenadas):
    """
     Aplica los filtros seleccionados por el usuario siguiendo
     el orden de importancia indicado en categorias_ordenadas.

    Si una condición elimina todos los conciertos disponibles,
    se solicita una nueva preferencia para esa categoría hasta
    obtener al menos un resultado o se continua si el usuario lo desea. 

    Parameters:
        df_filtrado (DataFrame): dataset sobre el cual se aplican
        los filtros.

        dic_preferencias (dict): preferencias seleccionadas por
        el usuario.

        categorias_ordenadas (list): categorías ordenadas según
        importancia.

    Retorno:
        DataFrame: dataset resultante luego de aplicar todos los
        filtros.
       

    Manejo de errores:
        - Si una condición elimina todos los conciertos
          disponibles, se solicita una nueva preferencia.
        - Las validaciones específicas de cada dato son realizadas
          por las funciones que solicitan las preferencias.
    """

    ## Se recorren las categorías desde la más importante
    ## hasta la menos importante.
    for categoria in categorias_ordenadas:

        while True:

            ## Se obtiene la preferencia asociada a la categoría.
            condicion = dic_preferencias[categoria]

            ## Se prueba el filtro sobre el dataset actual.
            resultado_filtro = filtrar_por_condicion(
                df_filtrado,
                categoria,
                condicion
            )

            ## Si todavía quedan conciertos,
            ## se acepta el filtro.
            if len(resultado_filtro) > 0:

                df_filtrado = resultado_filtro

                ## Se pasa a la siguiente categoría.
                break

            ## Si el filtro elimina todos los conciertos,
            ## se pide una condición más amplia.
            print(f"La condición elegida para '{categoria}' elimina todos los conciertos disponibles.")
            decision=input(f"Si desea modificar su preferencia elija 1. Si desea continuar sin coincidencias de {categoria} ingrese 2")
            while decision not in ["1", "2"]:
                print("Opción inválida. Debe elegir 1 o 2")
                decision=input(f"Si desea modificar su preferencia elija 1. Si desea continuar sin coincidencias de {categoria} ingrese 2")
            if decision == "1":
                print("Por favor ingrese una preferencia más amplia.")
                ## Esta función deberá llamar internamente
                ## a la función correspondiente según la categoría.
                nueva_condicion = pedir_nueva_preferencia(
                categoria,
                df_filtrado)
                dic_preferencias[categoria] = nueva_condicion
            elif decision=="2": 
                print(f"Eligió la opción de continuar, por lo tanto no habrá coincidencias con {categoria}")
                break
            ## Se actualiza el diccionario para volver
            ## a intentar el filtrado.
    

    ## Cada filtro trabaja sobre el resultado del filtro anterior.
    ## Por eso, al finalizar, df_filtrado contiene únicamente los
    ## conciertos que cumplen todas las condiciones.

    return df_filtrado
