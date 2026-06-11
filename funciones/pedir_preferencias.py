#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 20:23:30 2026

@author: victoriamochnacs
"""

import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def ordenar_preferencias (lista_categorias): #FUNCIÓN DE EMI
    pass


def pedir_preferencias(df, categorias_ordenadas):
    """
    Descripción: Solicita al usuario sus preferencias siguiendo el
    orden de categorías indicado. Las preferencias seleccionadas se
    guardan en un diccionario para ser utilizadas posteriormente
    durante el filtrado del dataset.

    Parameters:
        df (DataFrame): dataframe de conciertos.
        categorias_ordenadas (list): lista con las categorías ordenadas por el usuario según su prioridad.

    Return:
        dict - diccionario cuyas claves son las categorías de filtrado
        y cuyos valores son las preferencias seleccionadas por el usuario.
    """

    dict_preferencias = {}

    for categoria in categorias_ordenadas:

        if categoria == "genero":
            dict_preferencias["genero"] = pedir_generos(
                df["Género musical"])

        elif categoria == "precio":
            dict_preferencias["precio"] = pedir_rango_precios()

        elif categoria == "fecha":
            dict_preferencias["fecha"] = pedir_fechas()

        elif categoria == "horario":
            dict_preferencias["horario"] = pedir_franja_horaria()

        elif categoria == "ubicacion":
            dict_preferencias["ubicacion"] = pedir_ubicacion(df)
#falta agregar el llamado a la funcion de asientos disponibles
    return dict_preferencias

#PEDIR GÉNEROS
def pedir_generos(columna_generos): #de donde viene "columna_generos"
    """
    Descripción: Muestra los géneros disponibles, permite al usuario
    seleccionar uno o más géneros mediante su ID y devuelve los géneros
    elegidos.

    Parameters:
        columna_generos (Series): columna que contiene los géneros musicales.

    Return:
        lista_generos: lista con los géneros seleccionados por el usuario.

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
    #.drop _duplicates() es un método que elimina los géneros repetidos de la columna
    #.reset_index(drop=True) reorganiza los índices de la columna sin repetidos
    tabla_generos = pd.DataFrame({
        "id": range(1, len(generos_sin_repetir) + 1),
        "genero": generos_sin_repetir})
    #crea un nuevo DataFrame con una columna ID (que sería el id del género), y con otra columna de los generos sin repetir.
    

    print("Esto son los géneros disponibles.")
    print(tabla_generos)
    #Se muestra la tabla/DataFrame de los géneros sin repetir con al columna de id, entonces cada id se corresponde a cada género.

    generos_seleccionados = []
    #Es la lista en donde se van a guardar los géneros que elige el usuario.
    while True:
        opcion = input("Ingrese el ID de un género que se encuentre en la tabla y le interese "
            "(o escriba 'fin'): ")
        #Dentro de un ciclo while se le pide al usuario que ingrese un numero o fin. Por lo tanto, se verá que si el usuario ingresa 
        #un dato erróneo (str que no sea fin, bool, numero negativo, etc) se llega al final del ciclo y automáticamente vuelve a comenzar
        #volviendo a pedirle que ingrese un género   (numero) o "fin"

        if opcion.lower() == "fin":
#si el ingreso del usuario en minúscula es igual a fin, entonces:
            if len(generos_seleccionados) == 0: #se fija si la lista de generos_seleccionados tiene elementos o no: 
                print("Debe seleccionar al menos un género.")    #si no tiene, se reinicia el ciclo while. 
              
            else:
                break
    #Si sí tiene, entonces se corta el ciclo while (con el break)
        else:
            try:
                opcion = int(opcion)
                if opcion < 1 or opcion > len(tabla_generos):
                    print("El ID ingresado no existe.")
                else:
                    genero = tabla_generos.loc[
                        tabla_generos["ID"] == opcion,
                        "Genero"].iloc[0]
                    if genero in id_generos_seleccionados:
                        print("Ese género ya fue seleccionado.")
                    else:
                        id_generos_seleccionados.append(genero)
                        print(f"Se agregó: {genero}")

            except ValueError:
                print("Debe ingresar un número válido o 'fin'.")
    
    generos_seleccionados = []
    for id in id_generos_seleccionados:
        genero = tabla_generos.loc[id,"Género"]
        generos_seleccionados.append(genero)

    return generos_seleccionados

def pedir_rango_precios ():
    print("💰 Definición de rango de precio buscado: Ajuste sus preferencias para encontrar un concierto acorde a su presupuesto")
    while True:
        try:
            precio_min = float(input("Ingrese el mínimo de precio que esté dispuesto a pagar por el concierto"))
            precio_max = float(input("Ingrese el máximo de precio que esté dispuesto a pagar por el concierto"))
            if precio_min > precio_max:
                raise ValueError ("El valor del precio máximo es menor al precio mínimo. Ingresar nuevamente")
        except ValueError as e:
            print (f"Error: {e} o alguno de los valores no es un número. Ingresar de nuevo correctamente.")
        else: 
            precios = {"min": precio_min, 
                       "max": precio_max}
            break
    return precios

##Para pedir fecha o rango de fechas
from datetime import datetime

def pedir_fechas():
    """
    Descripción: Solicita al usuario una fecha específica o un rango de
    fechas. Si desea consultar un único día, debe ingresar la misma fecha
    para fecha_1 y fecha_2.

    Parámetros:
        Ninguno.

    Retorno:
        dict - diccionario con las fechas seleccionadas.

        Formato:
        {"fecha_1": "DD/MM/AA",
         "fecha_2": "DD/MM/AA"}

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
        print ("Ahora, elija la fecha o rango de fechas para realizar la búsqueda de conciertos. Si quiere buscar un concierto en una fecha en específico, ingrese la misma fecha inicial y final")
        try:

            dia_fecha_1 = input("Ingrese el día de la fecha inicial: Si es un número menor a 10, incluir el 0 del principio (Por ejemplo, 01)")
            mes_fecha_1 = input("Ingrese el mes de la fecha inicial. Si es un número menor a 10, incluir el 0 del principio (Por ejemplo, 04)")
            año_fecha_1 = input ("Ingrese el año de la fecha inicial.")
            
            fecha_1 = f"{dia_fecha_1}/{mes_fecha_1}/{año_fecha_1}"

            fecha_1 = datetime.strptime(fecha_1, "%d/%m/%y").date()

            if fecha_1 < fecha_actual:
                print("La fecha inicial no puede ser anterior a hoy.")
                continue

            dia_fecha_2 = input("Ingrese el día de la fecha final: Si es un número menor a 10, incluir el 0 del principio (Por ejemplo, 01)")
            mes_fecha_2 = input("Ingrese el mes de la fecha final. Si es un número menor a 10, incluir el 0 del principio (Por ejemplo, 04)")
            año_fecha_2 = input ("Ingrese el año de la fecha final.")
            
            fecha_2 = f"{dia_fecha_2}/{mes_fecha_2}/{año_fecha_2}"

            fecha_2 = datetime.strptime(fecha_1, "%d/%m/%y").date()

            if fecha_2 < fecha_1:
                print("La fecha final no puede ser anterior a la fecha inicial.")
                continue #este continue no se si tiene que estar, o si vuelve automaticamente

            return {"fecha_1": fecha_1,
                "fecha_2": fecha_2}
        
            break 

        except ValueError:

            print("Fecha inválida. Utilice el formato DD/MM/AA y verifique que la fecha exista.")
   

def pedir_franja_horaria ():
    '''
    Esta función se encarga de pedirle una franja horaria al usuario.

    Returns
    -------
    El formato de retorno sería: {"hora_min": hora_min
                                  "hora_max": hora_max}

    '''
    
    print ("En esta sección, ingrese una franja horaria para la que desee buscar un concierto. Aclaración: Esta búsqueda no contempla toda la duración del concierto. Es decir, va a utilizarse para buscar conciertos que comiencen dentro de la franja horaria ingresada, pero no considera si el evento termina después del horario indicado como su máximo" )
    
    while True:
        hora_1 = input ("Ingrese la hora mínima")
        minutos_1 = input ("Ingrese los minutos de la hora mínima")
        
        hora_min = f"{hora_1}:{minutos_1}"
        
        hora_2 = input ("Ingrese la hora máxima")
        minutos_2 = input ("Ingrese los minutos máximos")
        
        hora_max = f"{hora_2}:{minutos_2}"
        
        try:
            hora_min = pd.to_datetime (hora_min, format = '%H:%M').strftime('%H:%M')
            hora_max = pd.to_datetime (hora_max, format = '%H:%M').strftime('%H:%M')
        
            if hora_max < hora_min:
                raise ValueError ("La hora mínima no puede ser después de la hora máxima")
                continue
            
            
        except ValueError as e:
            print



def pedir_distancia_max(df):
    while True: 
         try:
             distancia_max=float(input("Ingrese la distancia maxima en km que estaría dispuesto a viajar: "))
         except ValueError: 
             print("El ingreso debe ser un float. Vuelva a ingresar una distancia máxima")
         else:
             if distancia_max<=0: 
                 print("La distancia debe ser mayor que cero. Vuelva a ingresar una distancia máxima")
             else:
                 break
    return distancia_max
            
def pedir_ubicacion_partida(df, dist_max ): 
    #FALTA DOCSTRING, YA SE
   while True: 
        direccion_usuario=input("Ingrese su ubicación de partida: ")
        if direccion_usuario.strip()==" ":
           print("El ingreso de la dirección no puede estar vacío. Porfavor, vuelva a ingresar su ubicación de partida")
        else:
            break
   lista_distancias= calcular_distancias(df["direccion"], dist_max, direccion_usuario) #se llama a funcion que devuelve lista de distancias
   df["distancias"]=lista_distancias #agrega una columna de "distancias" cuyos valores es la lista que devolvió la función calcular_distancias
   
   return df
    
def calcular_distancias(columna_direcciones, distancia_max, direccion_usuario):
    geolocalizador= Nominatim(user_agent= "calculador_distancias")
   
    ubicacion_usuario=geolocalizador.geocode(direccion_usuario)
    
    latitud_usuario=ubicacion_usuario.latitude
    longitud_usuario=ubicacion_usuario.longitude
    
    lista_distancias=[ ]
    for direccion in columna_direcciones:
        ubicacion_evento=geolocalizador.geocode(direccion)
       
        latitud_evento=ubicacion_evento.latitude
        longitud_evento=ubicacion_evento.longitude
       
        distancia= geodesic((latitud_usuario, longitud_usuario), (latitud_evento, longitud_evento)).kilometers
        lista_distancias.append(distancia)
    return lista_distancias
                
#las funciones pedir_ubicacion_partida, calcular_distancias y pedir_distancia_max no estan completas. Tenemos que ver cómo se comunican entre sí y con las funciones de filtrado.
