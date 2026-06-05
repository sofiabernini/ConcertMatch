# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 09:02:21 2026

@author: angie
"""

def pedir_ubicacion_distancia_max(): 
    direccion_usuario=input("Ingrese su ubicación: ")
    if direccion_usuario.strip()==" ":
        raise ValueError ("El ingreso de la ubicación no puede estar vacío. Error en función pedir_ubicacion_distancia_max")
    while True: 
        try:
            distancia_max=float(input("Ingrese la distancia maxima en km que estaría dispuesto a viajar: "))
        except ValueError: 
            print("El ingreso debe ser un float. Error en función pedir_ubicacion_distancia_max")
        else: 
            if distancia_max<=0: 
                print("La distancia debe ser mayor que cero. Error en función pedir_ubicacion_distancia_max")
        
            
            
        