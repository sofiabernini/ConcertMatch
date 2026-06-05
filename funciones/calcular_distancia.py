# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 08:40:03 2026

@author: angie
"""

from geopy.geocoders import Nominatim 
#sirve para transformar una dirección en coordenadas (a través de atributos .longitude o .latitude)
from geopy.distance import geodesic
#sirve para calcular la distancia entre dos coordenadas

def calcular_distancia(direccion, columna_ubicacion):
    """
    Convierte direcciones en coordenadas y calcula la distancia entre ellas.

    Parameters
    ----------
    dirección : str
        Es la dirección del usuario.
    columna_ubicacion : serie
        Es la columna "ubicacion" del DataFrame.

    Returns
    -------
    None.

    """
    