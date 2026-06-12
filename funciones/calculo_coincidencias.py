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
from funciones.pedir_preferencias import pedir_preferencias #no sé si lo voy a usar todavía
 
#el df todavía no sé de qué función lo saco así que lo dejo como "df" solo.  
# lo mismo con las preferencias. Lo tengo que llamar desde la función de pedir_preferencias
    
def calcular_coincidencias(df_filtrado, preferencias):

    df = df_filtrado.copy() #esto no sé de qué es

# GÉNERO 
    generos_usuario = preferencias["genero"]

    def calc_genero(genero_concierto):
        if genero_concierto.lower().strip() in generos_usuario:
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
            return 1.0 - (p / pmax) #hicimos el cálculo de esta manera porque, asumimos que cuanto más barato, más utilidad
        else:
            return 0.0
    #se crea una columna "coincidencia_precio" en el df
    df["coincidencia_precio"] = df_filtrado["Precio final"].apply(calc_precio)

# FECHA 
    f_min = preferencias["fecha"]["min"]
    f_max = preferencias["fecha"]["max"]

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
    h_min = preferencias["horario"]["min"]
    h_max = preferencias["horario"]["max"]

    def calc_horario(h):
        if h_min <= h <= h_max:
            return 1.0
        else:
            return 0.0

    df["coincidencia_horario"] = df["Horario"].apply(calc_horario)

# DISTANCIA 
    d_max = preferencias["ubicación"] #revisar esto

    def calc_distancia(d):
        if d > d_max:
            return 0.0
        else:
            return 1.0 - (d / d_max)

    df["coincidencia_distancia"] = df["distancias"].apply(calc_distancia)

    # ── ASIENTOS ─────────────────────────────────────────────
    necesita = preferencias["asientos"] #revisar esto 

    def calc_asientos(tiene):
        if necesita and not tiene:
            return 0.0
        else:
            return 1.0

    df["coincidencia_asientos"] = df["Lugar para sentarse"].apply(calc_asientos)

    return df    
            

def ponderacion_total (df_filtrado, preferencias): #hay que conectarlo desde main o no sé desde donde
    #acá voy a llamar a calcular_coincidencias, así que voy a llamar solo a esta función desde el main
    
    df = calcular_coincidencias(df_filtrado, preferencias)
    
    # acá df ya tiene las columnas coincidencia_genero, coincidencia_precio, etc.
    # y podés seguir trabajando con ellas    
    




