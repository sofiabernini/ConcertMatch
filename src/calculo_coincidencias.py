#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 20:27:55 2026

@author: victoriamochnacs
"""

#este archivo contiene funciones que calculan el valor de cada categoria según su coincidencia y luego el cálculo final de ponderacion
#contiene la funcion
#   -calcular_coincidencias
#   -ponderacion_total
 
#el df todavía no sé de qué función lo saco así que lo dejo como "df" solo.  
# lo mismo con las preferencias. Lo tengo que llamar desde la función de pedir_preferencias
    
def calcular_coincidencias(df_filtrado, preferencias):

    df = df_filtrado.copy() #Hace una copia del DataFrame para no modificar el original.

# GÉNERO 
    generos_usuario = preferencias["genero"]
    generos_usuario_min = []
    for genero in generos_usuario:
        genero = genero.lower().strip()
        generos_usuario_min.append(genero)

    def calc_genero(genero_concierto):
        if genero_concierto.lower().strip() in generos_usuario_min:
            return 1.0
        else:
            return 0.0
    #se crea una columna "coincidencia_genero" en el df
    df["coincidencia_genero"] = df_filtrado["Género musical"].apply(calc_genero)

# PRECIO 
    pmin = preferencias["precio"]["min"]
    pmax = preferencias["precio"]["max"]

    def calc_precio(p):
        if p < pmin:
            return 1.0
        elif pmin <= p <= pmax:
            return 1.0
        else:
            return 0.0
    #se crea una columna "coincidencia_precio" en el df
    df["coincidencia_precio"] = df_filtrado["Precio final"].apply(calc_precio)

# FECHA 
    f_min = preferencias["fecha"]["fecha_1"]
    f_max = preferencias["fecha"]["fecha_2"]

    def calc_fecha(f):
        #CASO DE FECHA EXACTA
        if f_min == f_max:          
            if f == f_min:
                return 1.0
            else:
                return 0.0
        #CASO RANGO DE FECHAS
        else:                     
            if f_min <= f <= f_max:
                return 1.0
            else:
                return 0.0

    df["coincidencia_fecha"] = df["Fecha"].apply(calc_fecha)

# HORARIO 
    h_min = preferencias["horario"]["hora_min"]
    h_max = preferencias["horario"]["hora_max"]

    def calc_horario(h):
        if h_min <= h <= h_max:
            return 1.0
        else:
            return 0.0

    df["coincidencia_horario"] = df["Horario"].apply(calc_horario)

# DISTANCIA 
    d_max = preferencias["distancia"] #revisar esto

    def calc_distancia(d):
        if d > d_max:
            return 0.0
        else:
            return 1.0 - (d / d_max)

    df["coincidencia_distancia"] = df["distancias"].apply(calc_distancia)

# ── ASIENTOS ─────────────────────────────────────────────
    necesita = preferencias["lugar para sentarse"] #revisar esto 

    def calc_asientos(tiene):
        if necesita and not tiene:
            return 0.0
        else:
            return 1.0

    df["coincidencia_lugar para sentarse"] = df["Lugar para sentarse"].apply(calc_asientos)

    return df    
            

def ponderacion_total (df_filtrado, preferencias): #hay que conectarlo desde main o no sé desde donde
    #acá voy a llamar a calcular_coincidencias, así que voy a llamar solo a esta función desde el main
    
    df = calcular_coincidencias(df_filtrado, preferencias)
    
    # acá df ya tiene las columnas coincidencia_genero, coincidencia_precio, etc.
    # y podés seguir trabajando con ellas    

    categorias_en_orden = list(preferencias.keys())
    # por ejemplo: ["genero", "precio", "fecha", "horario", "ubicacion", "asientos"]
    
    
    if len(categorias_en_orden) == 0:
        raise ValueError ("No se puede hacer el cálculo de ponderación final")
        
    pesos = [0.35, 0.25, 0.15, 0.10, 0.10, 0.05]

    porcentajes = [] #se crea la lista para crear después una columna con el porcentaje de coincidencias

    #df.interrows() itera sobre todas las filas del df filtrado. suma las coincidencias de cada fila
    for i, fila in df.iterrows():
        total = (fila["coincidencia_" + categorias_en_orden[0]] * pesos[0] +
                 fila["coincidencia_" + categorias_en_orden[1]] * pesos[1] +
                 fila["coincidencia_" + categorias_en_orden[2]] * pesos[2] +
                 fila["coincidencia_" + categorias_en_orden[3]] * pesos[3] +
                 fila["coincidencia_" + categorias_en_orden[4]] * pesos[4] +
                 fila["coincidencia_" + categorias_en_orden[5]] * pesos[5])
        
        #transforma a porcentaje
        porcentajes.append(round(total * 100, 2))
    
    #crea una columna con el nombre "porcentaje_coincidencia" y con los datos de la lista "porcentajes"
    df["porcentaje_coincidencia"] = porcentajes
    
    
    #retorna el df con la columna incorporada
    return df   
  

############# NUEVOOO  
from datetime import datetime, date


def calcular_coincidencias(df_filtrado, dic_preferencias):
    """
    Descripción:
        Calcula el grado de coincidencia de cada concierto con las
        preferencias originales del usuario para cada categoría.

        Agrega una columna de coincidencia por categoría con valores
        entre 0 y 1, donde:
            - 1 representa la máxima coincidencia.
            - 0 representa que el concierto no cumple la preferencia.

    Parámetros:
        df_filtrado (DataFrame): DataFrame resultante luego de aplicar
        los filtros.

        dic_preferencias (dict): Diccionario con las preferencias
        originales del usuario.

    Retorno:
        DataFrame con las columnas de coincidencia agregadas.

    Manejo de errores:
        - No realiza validaciones sobre las preferencias, ya que fueron
          verificadas por las funciones que las solicitan.
        - Evita divisiones por cero cuando el rango de una categoría es
          nulo.
    """

    ## Se trabaja sobre una copia para no modificar el DataFrame recibido.
    df = df_filtrado.copy()

    # ==========================================================
    # GÉNERO
    # ==========================================================

    generos = dic_preferencias["genero"]["seleccionados"]
    favorito = dic_preferencias["genero"]["favorito"]

    def calc_genero(genero_concierto):
        """
        Calcula la coincidencia del género.
        """

        genero_concierto = genero_concierto.strip().lower()

        if genero_concierto == favorito.lower():
            return 1

        elif genero_concierto in [
            genero.lower()
            for genero in generos
        ]:
            return 0.8

        else:
            return 0

    ## Se agrega la columna de coincidencia de género.
    df["coincidencia_genero"] = df["Género musical"].apply(
        calc_genero
    )

    # ==========================================================
    # PRECIO
    # ==========================================================

    precio_min = dic_preferencias["precio"]["min"]
    precio_max = dic_preferencias["precio"]["max"]

    def calc_precio(precio):
        """
        Calcula la coincidencia del precio.
        """

        ## Si está fuera del rango elegido, no coincide.
        if precio < precio_min or precio > precio_max:
            return 0

        rango = precio_max - precio_min

        ## Si el usuario indicó un único precio.
        if rango == 0:
            return 1

        ## Cuanto más cercano al precio mínimo,
        ## mayor será la coincidencia.
        return 1 - ((precio - precio_min) / rango)

    df["coincidencia_precio"] = df["Precio final"].apply(
        calc_precio
    )

    # ==========================================================
    # FECHA
    # ==========================================================

    fecha_1 = dic_preferencias["fecha"]["fecha_1"]
    fecha_2 = dic_preferencias["fecha"]["fecha_2"]
    fecha_ideal = dic_preferencias["fecha"]["ideal"]

    def calc_fecha(fecha):
        """
        Calcula la coincidencia de la fecha.
        """

        ## Si está fuera del rango, no coincide.
        if fecha < fecha_1 or fecha > fecha_2:
            return 0

        rango = (fecha_2 - fecha_1).days

        ## Si el usuario eligió un único día.
        if rango == 0:
            return 1

        diferencia = abs(
            (fecha - fecha_ideal).days
        )

        ## Cuanto más cercana a la fecha ideal,
        ## mayor será la coincidencia.
        return 1 - (diferencia / rango)

    df["coincidencia_fecha"] = df["Fecha"].apply(
        calc_fecha
    )

    # ==========================================================
    # HORARIO
    # ==========================================================

    hora_1 = dic_preferencias["horario"]["hora_1"]
    hora_2 = dic_preferencias["horario"]["hora_2"]
    hora_ideal = dic_preferencias["horario"]["ideal"]

    def calc_horario(hora):
        """
        Calcula la coincidencia del horario.
        """

        ## Si está fuera del rango, no coincide.
        if hora < hora_1 or hora > hora_2:
            return 0

        rango = (
            datetime.combine(date.today(), hora_2)
            -
            datetime.combine(date.today(), hora_1)
        ).total_seconds()

        ## Si el usuario eligió un único horario.
        if rango == 0:
            return 1

        diferencia = abs(
            (
                datetime.combine(date.today(), hora)
                -
                datetime.combine(date.today(), hora_ideal)
            ).total_seconds()
        )

        ## Cuanto más cercano al horario ideal,
        ## mayor será la coincidencia.
        return 1 - (diferencia / rango)

    df["coincidencia_horario"] = df["Horario"].apply(
        calc_horario
    )

    # ==========================================================
    # DISTANCIA
    # ==========================================================

    distancia_max = dic_preferencias["distancia"]

    def calc_distancia(distancia):
        """
        Calcula la coincidencia de la distancia.
        """

        ## Si supera la distancia máxima elegida,
        ## no coincide.
        if distancia > distancia_max:
            return 0

        ## Evita división por cero.
        if distancia_max == 0:
            return 1

        ## Cuanto más cerca esté el concierto,
        ## mayor será la coincidencia.
        return 1 - (distancia / distancia_max)

    df["coincidencia_distancia"] = df["distancias"].apply(
        calc_distancia
    )

    # ==========================================================
    # ASIENTOS
    # ==========================================================

    necesita_asientos = dic_preferencias["cuenta con asientos"]

    def calc_asientos(tiene_asientos):
        """
        Calcula la coincidencia respecto a la disponibilidad
        de asientos.
        """

        if necesita_asientos:

            if tiene_asientos:
                return 1

            return 0

        ## Si el usuario no considera importante esta categoría,
        ## todos los conciertos reciben coincidencia máxima.
        return 1

    df["coincidencia_cuenta con asientos"] = df[
        "Cuenta con asientos"
    ].apply(calc_asientos)

    ## Devuelve el DataFrame con todas las columnas de
    ## coincidencia agregadas.
    return df

