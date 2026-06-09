# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 16:25:54 2026

@author: angie
"""
import pandas as pd
def obtener_criterios_filtro(df, categorias_ordenadas):
    """
    Descripción: Solicita al usuario sus preferencias siguiendo el
    orden de categorías indicado. Las preferencias seleccionadas se
    almacenan en un diccionario para ser utilizadas posteriormente
    durante el filtrado del dataset.

    Parámetros:
        df (DataFrame) - dataset de conciertos.
        categorias_ordenadas (list) - lista con las categorías
        ordenadas por el usuario según su prioridad.

    Retorno:
        dict - diccionario cuyas claves son las categorías de filtrado
        y cuyos valores son las preferencias seleccionadas por el usuario.

    Manejo de errores:
        - Los errores de ingreso de datos son gestionados por las
          funciones específicas de cada categoría
          (pedir_generos, pedir_artistas, etc.).
        - Si una categoría no corresponde a ninguna de las esperadas,
          se ignora y el programa continúa.
    """

    criterios_filtro = {}

    for categoria in categorias_ordenadas:

        if categoria == "género":
            criterios_filtro["género"] = pedir_generos(
                df["Género musical"])

        elif categoria == "artista":
            criterios_filtro["artista"] = pedir_artistas(
                df["Nombre del artista/banda"])

        elif categoria == "precio":
            criterios_filtro["precio"] = pedir_precio()

        elif categoria == "fecha":
            criterios_filtro["fecha"] = pedir_fechas()

        elif categoria == "horario":
            criterios_filtro["horario"] = pedir_horarios()

        elif categoria == "ubicación":
            criterios_filtro["ubicación"] = pedir_ubicacion()

    return criterios_filtro

def pedir_generos(columna_generos):
    """
    Descripción: Muestra los géneros disponibles, permite al usuario
    seleccionar uno o más géneros mediante su ID y devuelve los géneros
    elegidos.

    Parámetros:
        columna_generos (Series) - columna que contiene los géneros musicales.

    Retorno:
        list - lista con los géneros seleccionados por el usuario.

    Manejo de errores:
        - Si el usuario ingresa un valor que no puede convertirse a entero,
          se muestra un mensaje de error y se vuelve a pedir el dato.
        - Si el usuario ingresa un ID inexistente, se informa el error y se
          permite reintentar.
        - Si el usuario intenta finalizar sin haber seleccionado ningún género,
          se le solicita que elija al menos uno.
        - Si el usuario intenta seleccionar un género ya elegido, se informa
          que ese género ya fue agregado.
    """

    generos_sin_repetir = columna_generos.drop_duplicates().reset_index(drop=True)

    tabla_generos = pd.DataFrame({
        "ID": range(1, len(generos_sin_repetir) + 1),
        "Genero": generos_sin_repetir})

    print("\nGÉNEROS DISPONIBLES")
    print(tabla_generos)

    generos_seleccionados = []

    while True:
        opcion = input(
            "\nIngrese el ID de un género que se encuentre en la tabla y le interese "
            "(o escriba 'fin'): ")

        if opcion.lower() == "fin":

            if len(generos_seleccionados) == 0:
                print("Debe seleccionar al menos un género.")
            else:
                break
        else:
            try:
                opcion = int(opcion)
                if opcion < 1 or opcion > len(tabla_generos):
                    print("El ID ingresado no existe.")
                else:
                    genero = tabla_generos.loc[
                        tabla_generos["ID"] == opcion,
                        "Genero"].iloc[0]
                    if genero in generos_seleccionados:
                        print("Ese género ya fue seleccionado.")
                    else:
                        generos_seleccionados.append(genero)
                        print(f"Se agregó: {genero}")

            except ValueError:
                print("Debe ingresar un número válido o 'fin'.")

    return generos_seleccionados

##para pedir fecha o rango de fechas
from datetime import datetime

def pedir_fecha():
    """
    Descripción: Solicita al usuario una fecha específica o un rango de
    fechas. Si desea consultar un único día, debe ingresar la misma fecha
    para fecha_1 y fecha_2.

    Parámetros:
        Ninguno.

    Retorno:
        dict - diccionario con las fechas seleccionadas.

        Formato:
        {
            "fecha_1": "DD/MM/AA",
            "fecha_2": "DD/MM/AA"
        }

    Manejo de errores:
        - Si el formato ingresado no es DD/MM/AA se informa el error.
        - Si la fecha no existe se informa el error.
        - Si la fecha inicial es anterior a la fecha actual se informa el error.
        - Si la fecha final es anterior a la fecha inicial se informa el error.
        - Se permite reintentar hasta ingresar datos válidos.

    Raises:
        No hay. Todos los errores son manejados dentro de la función.
    """

    fecha_actual = datetime.now().date()

    while True:

        try:

            fecha_1_str = input(
                "Ingrese la fecha inicial (DD/MM/AA): "
            )

            fecha_1 = datetime.strptime(
                fecha_1_str,
                "%d/%m/%y"
            ).date()

            if fecha_1 < fecha_actual:
                print(
                    "La fecha inicial no puede ser anterior a hoy."
                )
                continue

            fecha_2_str = input(
                "Ingrese la fecha final (DD/MM/AA): "
            )

            fecha_2 = datetime.strptime(
                fecha_2_str,
                "%d/%m/%y"
            ).date()

            if fecha_2 < fecha_1:
                print(
                    "La fecha final no puede ser anterior a la fecha inicial."
                )
                continue

            return {
                "fecha_1": fecha_1_str,
                "fecha_2": fecha_2_str
            }

        except ValueError:

            print(
                "Fecha inválida. Utilice el formato DD/MM/AA y verifique que la fecha exista."
            )
