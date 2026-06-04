# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 16:31:39 2026

@author: angie
"""

#esto es un borrador
def filtrar_dataset(df, columna, operador, valor):

    if operador == "==":
        return df[df[columna] == valor]

    elif operador == "<=":
        return df[df[columna] <= valor]

    elif operador == ">=":
        return df[df[columna] >= valor]