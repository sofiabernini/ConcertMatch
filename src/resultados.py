# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 16:34:42 2026

@author: sofia
"""
def obtener_columna_importante(categorias_ordenadas):
    """
    Descripción:
        Determina cuál es la categoría más importante entre
        precio y distancia según el orden elegido por el usuario.

    Parámetros:
        categorias_ordenadas (list): categorías ordenadas por el
        usuario según su prioridad.

    Retorno:
        str:
            "Precio final" si precio tiene mayor prioridad.
            "distancias" si distancia tiene mayor prioridad.

    Manejo de errores:
        No realiza validaciones ya que las categorías fueron
        verificadas previamente.
    """

    ## Se recorren las categorías respetando el orden elegido.
    for categoria in categorias_ordenadas:

        if categoria == "precio":

            return "Precio final"

        elif categoria == "distancia":

            return "distancias"

def ordenar_resultados(df_filtrado, columna_importante):
    """
    Descripción:
        Ordena los conciertos de menor a mayor según la
        columna indicada.

    Parámetros:
        df_filtrado (DataFrame): conciertos luego del filtrado.

        columna_importante (str): columna utilizada para ordenar.

    Retorno:
        DataFrame: conciertos ordenados.

    Manejo de errores:
        No realiza validaciones ya que los parámetros fueron
        obtenidos previamente.
    """

    ## Ordena de menor a mayor.
    df_ordenado = df_filtrado.sort_values(by=columna_importante, ascending=True)

    return df_ordenado

def mostrar_info_resultados(df_ordenado):
    """
    Descripción:
        Muestra por pantalla los cinco primeros conciertos del
        DataFrame ordenado. Si hay menos de cinco conciertos,
        muestra todos los disponibles.

    Parámetros:
        df_ordenado (DataFrame): conciertos ordenados según la
        categoría más importante.

    Retorno:
        None

    Manejo de errores:
        No realiza validaciones ya que el DataFrame nunca llega
        vacío a esta función.
    """

    print("=" * 50)
    print("⭐ CONCIERTOS RECOMENDADOS ⭐")
    print("=" * 50)

    ## Se recorren únicamente los primeros cinco conciertos.
    for _, fila in df_ordenado.head(5).iterrows():

        print(f"🎵 Artista/Banda: {fila['Artista/Banda']}")
        print(f"   - Género: {fila['Género musical']}")
        print(f"   - Precio: ${fila['Precio final']}")
        print(f"   - Fecha: {fila['Fecha']}")
        print(f"   - Horario: {fila['Horario']}")
        print(f"   - Lugar: {fila['Estadio/Predio']}")
        print(f"   - Dirección: {fila['Ubicación']}")
        print(f"   - Distancia: {round(fila['distancias'], 2)} km")

        print(f"   - Acceso para movilidad reducida: " f"{'Sí' if fila['Acceso movilidad reducida'] else 'No'}")

        print(f"   - Cuenta con asientos: "  f"{'Sí' if fila['Lugar para sentarse'] else 'No'}")

        print(f"   - Link de la ticketera: {fila['Link ticketera']}")

        print("-" * 50)
