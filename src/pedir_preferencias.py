#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 20:23:30 2026

@author: victoriamochnacs
"""

import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import geodesic


def ordenar_preferencias():
    """
    Solicita al usuario que ordene sus preferencias de mayor a menor. Cada categoria corresponde a un numero diferente, el usuario deberá ingresar numeros  entre el 1 al 6 separados por coma. El ingreso del usuario se agrega a una lista. Se validara el ingreso del usuario, que el usuario ingrese un numero, que el numero ingresado este entre 1 y 6, que ingrese si o si 6 numero y que no ingrese numeros repetidos. Una vez validado, se traducen los numeros a sus categorias correcpondientes y devuelve una lista con las categorias ordenadas.
    
    Returns
    -------
    categorias_ordenadas : list
        lista de preferencias segun el orden de prioridad elegido por el usuario

    """
    
    preferencias = {
        "1": "Género",
        "2": "Precio",
        "3": "Fecha",
        "4": "Horario",
        "5": "Dirección",
        "6": "Cuenta con asientos"
    }
    while True:
          solicitar_orden= input("Ordená tus preferencias de mayor a menor importancia: 1) Género  2) Precio  3)   Fecha  4) Horario  5) Dirección  6) Cuenta con asientos. Ingresá los números separados por coma: ") # aosicé un numero a cada preferencia para que el usuario ingrese algo de este estilo : 5,4,3,6,1,2. En este caso eso seria equivalente a direccion, horario, fecha, cuenta con asientos,genero, precio. 

          lista_numeros=solicitar_orden.split(",") # con .split estos numeros pasan de verse asi 5,4,3,6,1,2 a estar separados en una lista, asi: ["5","4","3","6","1","2"]
          error= False
          for numero in lista_numeros:
              if not numero.isdigit (): # valida  que los valores  ingresados sean numeros 
                 print("Error: El  valor ingresado debe ser un numero ")
                 error=True
              elif numero not in ["1","2","3","4","5","6"]: # valida que que no hayan numeros distintos a 1 2 3 4 5 6 
                 print("Error: El numero ingresado debe estar entre 1 y 6")
                 error=True
          if error: # si el error es verdadero, vuelve a pedir las preferencias
             continue
         
          if len(lista_numeros)!= 6: # valido que el usuario haya ingresado si o si 6 numeros
             print("Error: se deben ingresar 6 preferencias")
             continue  # si no, vuelve a pedirle que ordene las preferencias
          if len(set(lista_numeros)) != 6: # el set lo que hace es extraer la cantidad de numeros que no estan repetidos, si el usuario ingreso 5,5,6,3,2,1. la lista quedaria de 5 elementos, es decir distinto de 6. 
             print("Error: No pueden haber numeros repetidos")
             continue # si la lista queda de distinto tamaño por tener numero repetidos, vuelve a pedirle las preferencias
          break 
    
    categorias_ordenadas = []
    for numero in lista_numeros:
        valor = preferencias[numero]
        categorias_ordenadas.append(valor)
    
    return categorias_ordenadas # devulevo algo de este estilo ["direccion", "horario"," fecha", "cuenta con asientos","genero", "precio"], 
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
                df["Género"])

        elif categoria == "precio":
            dict_preferencias["precio"] = pedir_rango_precios()

        elif categoria == "fecha":
            dict_preferencias["fecha/s"] = pedir_fechas()

        elif categoria == "horario":
            dict_preferencias["horario"] = pedir_franja_horaria()

        elif categoria == "direccion":
            dict_preferencias["direccion"] = pedir_distancia_max(df)
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
                    if genero in generos_seleccionados:
                        print("Ese género ya fue seleccionado.")
                    else:
                        generos_seleccionados.append(genero)
                        print(f"Se agregó: {genero}")

            except ValueError:
                print("Debe ingresar un número válido o 'fin'.")

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
            print ("Ingrese el valor nuevamente hasta que sea válido")
        
        else:
            break
            return {"hora_min": hora_min, "hora_max": hora_max}

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
            
def pedir_ubicacion_partida(df): 
    #FALTA DOCSTRING, YA SE
   while True: 
        direccion_usuario=input("Ingrese su dirección de partida: ")
        if direccion_usuario.strip()=="":
           print("El ingreso de la dirección no puede estar vacío. Porfavor, vuelva a ingresar su ubicación de partida")
        else: 
            geolocalizador= Nominatim(user_agent= "concertmatch")
            ubicacion_usuario=geolocalizador.geocode(direccion_usuario)
            if ubicacion_usuario is None: 
                print("La dirección no existe")
            else: 
                latitud_usuario=ubicacion_usuario.latitude
                longitud_usuario=ubicacion_usuario.longitude
                break
   lista_distancias= calcular_distancias(df["direccion"], latitud_usuario, longitud_usuario) #se llama a funcion que devuelve lista de distancias
   df["distancias"]=lista_distancias #agrega una columna de "distancias" cuyos valores es la lista que devolvió la función calcular_distancias
   
   return df
    
def calcular_distancias(columna_direcciones, latitud_usuario, longitud_usuario):
    geolocalizador= Nominatim(user_agent= "concertmatch")
    lista_distancias=[ ]
    for direccion in columna_direcciones:
        ubicacion_evento=geolocalizador.geocode(direccion)
       
        latitud_evento=ubicacion_evento.latitude
        longitud_evento=ubicacion_evento.longitude
       
        distancia= geodesic((latitud_usuario, longitud_usuario), (latitud_evento, longitud_evento)).kilometers
        lista_distancias.append(distancia)
    return lista_distancias
                
#las funciones pedir_ubicacion_partida, calcular_distancias y pedir_distancia_max no estan completas. Tenemos que ver cómo se comunican entre sí y con las funciones de filtrado.

## hay q ponerle bien el nombre de las funciones a las q llama.
def pedir_nueva_preferencia(categoria, df_filtrado):
    """
    Descripción:
        Solicita nuevamente una preferencia para la categoría indicada.

    Parámetros:
        categoria (str) - categoría para la cual se desea pedir una nueva condición.
        df_filtrado (DataFrame) - dataset actual. Se utiliza en aquellas funciones
        que necesitan información del dataset para mostrar opciones disponibles.

    Retorno:
        condición válida para la categoría solicitada.

    Manejo de errores:
        No realiza validaciones propias. Las validaciones son realizadas
        por las funciones llamadas internamente.
    """

    if categoria == "genero":

        return pedir_generos(
            df_filtrado["Género musical"]
        )

    elif categoria == "precio":

        return pedir_rango_precios()

    elif categoria == "fecha":

        return pedir_fechas()

    elif categoria == "horario":

        return pedir_franja_horaria()

    elif categoria == "distancia":

        return pedir_distancia_max()

    elif categoria == "cuenta con asientos":

        return pedir_asientos()
