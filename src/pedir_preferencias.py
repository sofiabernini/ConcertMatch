#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 20:23:30 2026

@author: victoriamochnacs
"""

import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import geodesic


def hacer_pregunta_si_no(mensaje):
    """
    Descripción: Se encarga de hacer una pregunta de si/no al usuario.
    Maneja los errores internamente y devuelve True (sí) o False (no).

    Parameters
    ----------
    mensaje : str
        Pregunta que se reponde con sí o no.

    Returns
    -------
    bool
        Devuelve True si el usuario respondió que sí o False si el usuario respondió que no.

    """
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta == "si":
            return True
        elif respuesta == "no":
            return False
        else:
            print("Opción no válida. Por favor, escribe 'si' o 'no'.")
            

def ordenar_preferencias():
    """
    Descripción: Solicita al usuario que ordene sus preferencias de mayor a menor. 
    Cada categoria corresponde a un numero diferente, el usuario deberá ingresar numeros entre el 1 al 6 separados por coma.
    El ingreso del usuario se agrega a una lista. 
    Validaciones: 
        -Que el usuario ingrese un numero, 
        -Que el numero ingresado este entre 1 y 6, 
        -Que ingrese si o si 6 números y que no ingrese numeros repetidos. 
    Una vez validado, se traducen los numeros a sus categorias correcpondientes y devuelve una lista con las categorias ordenadas.
    
    Returns
    -------
    categorias_ordenadas : list
        lista de preferencias segun el orden de prioridad elegido por el usuario

    """
    print ("🗒️ En esta sección, deberá ordenar las categorías que se presenten según sus preferencias. El orden deberá ser de mayor a menor nivel de importancia, y ese orden se aplicará a su búsqueda y al nivel de coincidencias")
    
    categorias = {
    "1": "genero",
    "2": "precio",
    "3": "fecha",
    "4": "horario",
    "5": "distancia",
    "6": "lugar para sentarse"}
    
    while True:
          solicitar_orden= input(f"Ordená tus preferencias de mayor a menor importancia:" 
                                 f"{categorias}" 
                                 "Ingresá los números separados por coma: ")
              
          # asoicié un numero a cada preferencia para que el usuario ingrese algo de este estilo : 5,4,3,6,1,2. En este caso eso seria equivalente a direccion, horario, fecha, cuenta con asientos,genero, precio. 

          lista_numeros=solicitar_orden.split(",") # con .split estos numeros pasan de verse asi 5,4,3,6,1,2 a estar separados en una lista, asi: ["5","4","3","6","1","2"]
          error= False
          for numero in lista_numeros:
              if not numero.isdigit (): # valida que los valores ingresados sean numeros 
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
        valor = categorias[numero]
        categorias_ordenadas.append(valor)
    
    return categorias_ordenadas # devulevo algo de este estilo ["direccion", "horario"," fecha", "cuenta con asientos","genero", "precio"]


def pedir_preferencias(df, categorias_ordenadas):
    """
    Descripción: Solicita al usuario sus preferencias siguiendo el
    orden de categorías indicado. Las preferencias seleccionadas se
    guardan en un diccionario para ser utilizadas posteriormente
    durante el filtrado del dataframe.

    Parameters:
        df (DataFrame): dataframe de conciertos/eventos.
        categorias_ordenadas (list): lista con las categorías ordenadas por el usuario según su prioridad.

    Return:
        dict_preferencias: diccionario cuyas claves son las categorías de filtrado
        y cuyos valores son las preferencias seleccionadas por el usuario.
    """

    dic_preferencias = {}

    for categoria in categorias_ordenadas:
        if categoria == "genero":
            dic_preferencias["genero"] = pedir_generos(df["Género musical"])
        elif categoria == "precio":
            dic_preferencias["precio"] = pedir_rango_precios()
        elif categoria == "fecha":
            dic_preferencias["fecha"] = pedir_fechas()
        elif categoria == "horario":
            dic_preferencias["horario"] = pedir_franja_horaria()
        elif categoria == "distancia":
            df = pedir_ubicacion_partida(df)
            dic_preferencias["distancia"] = pedir_distancia_max(df)
        elif categoria == "lugar para sentarse":
            dic_preferencias["lugar para sentarse"] = pedir_lugar_para_sentarse()
    return dic_preferencias, df

#PEDIR GÉNEROS
def pedir_generos(columna_generos): 
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
        "ID": range(1, len(generos_sin_repetir) + 1),
        "Género musical": generos_sin_repetir})
    #crea un nuevo DataFrame con una columna ID (que sería el id del género), y con otra columna de los generos sin repetir.
    

    print("Esto son los géneros disponibles.")
    print(tabla_generos)
    #Se muestra la tabla/DataFrame de los géneros sin repetir con al columna de id, entonces cada id se corresponde a cada género.

    generos_seleccionados = []
    #Es la lista en donde se van a guardar los géneros que elige el usuario.
    print ("🎙️ Elección de géneros musicales para la búsqueda. A continuación, se le presentará una lista con géneros asociados a un número (ID)." 
           "Usted va a ingresar los IDs de los géneros que desee seleccionar")
    while True:
        opcion = input("Ingrese el ID de un género que se encuentre en la tabla y le interese "
            "(o escriba 'fin' para terminar el proceso de ingreso de datos): ")
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
        else: #si la opción no es fin:
            try:
                opcion = int(opcion)
                if opcion < 1 or opcion > len(tabla_generos):
                    print("El ID ingresado no existe.")
                #si es un número menor a 1 o mayor a la cantidad de géneros disponibles, entonces le dice que la opción no existe. Vuelve a comenzar el ciclo while. 
                else:
                    genero = tabla_generos.loc[
                        tabla_generos["ID"] == opcion,
                        "Género musical"].iloc[0]
                #si el número sí existe como id, entonces busca el género correspondiente en la tabla.
                    if genero in generos_seleccionados:
                        print("Ese género ya fue seleccionado.")
                        #si ese género ya esta en la lista, le avisa al usuario y NO lo agrega. Vuelve a comenzar el ciclo while
                    else:
                        generos_seleccionados.append(genero)
                        print(f"Se agregó: {genero}")
                        #Si el género NO está en la lista, entonces lo agrega y vuelve a comenzar el ciclo while.

            except ValueError:
                print("Debe ingresar un número válido o 'fin'.")
                #si lo que ingresó no es un dato que se puede convertir a int, entonces se capta el error y vuelve a comenzar el ciclo while. 

    return generos_seleccionados #retorna la lista de géneros seleccionados

def pedir_rango_precios():
    print("💰 Definición del rango de precios buscado.")
    
    while True:
        try:
            precio_min = float(input("Ingrese el precio mínimo: "))
        except ValueError:
            print("Error: ingrese un número válido.")
            continue

        while True:
            try:
                precio_max = float(input("Ingrese el precio máximo: "))
            except ValueError:
                print("Error: ingrese un número válido.")
                continue

            if precio_max < precio_min:
                print("El precio máximo no puede ser menor al mínimo.")
                continue

            break  # precio_max válido
        break      # precio_min válido y precio_max válido

    return {"min": precio_min, "max": precio_max}

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
    print("📆 Definición de la fecha o rango de fechas de búsqueda, en formato DD/MM/AAAA. Se le va a pedir que complete día, mes y año que desee consultar." 
          "Si quiere buscar un concierto en una fecha en específico, ingrese la misma fecha inicial y final")
    while True:
        try:

            dia_fecha_1 = input("Ingrese el día (DD) de la fecha inicial: Si es un número menor a 10, incluir el 0 del principio (Por ejemplo, 01)")
            mes_fecha_1 = input("Ingrese el mes (MM) de la fecha inicial. Si es un número menor a 10, incluir el 0 del principio (Por ejemplo, 04)")
            año_fecha_1 = input ("Ingrese el año (AAAA) de la fecha inicial.")
            
            fecha_1 = f"{dia_fecha_1}-{mes_fecha_1}-{año_fecha_1}"

            fecha_1 = datetime.strptime(fecha_1, "%d-%m-%Y").date()

            if fecha_1 < fecha_actual:
                print("La fecha inicial no puede ser anterior a hoy.")
                continue

            dia_fecha_2 = input("Ingrese el día (DD) de la fecha final: Si es un número menor a 10, incluir el 0 del principio (Por ejemplo, 01)")
            mes_fecha_2 = input("Ingrese el mes (MM) de la fecha final. Si es un número menor a 10, incluir el 0 del principio (Por ejemplo, 04)")
            año_fecha_2 = input ("Ingrese el año (AAAA) de la fecha final.")
            
            fecha_2 = f"{dia_fecha_2}-{mes_fecha_2}-{año_fecha_2}"

            fecha_2 = datetime.strptime(fecha_2, "%d-%m-%Y").date()

            if fecha_2 < fecha_1:
                print("La fecha final no puede ser anterior a la fecha inicial.")
                continue #este continue no se si tiene que estar, o si vuelve automaticamente

            return {"fecha_1": fecha_1,
                "fecha_2": fecha_2}
        
        except ValueError:

            print("Fecha inválida. Utilice el formato DD/MM/AA y verifique que la fecha exista.")
   

def pedir_franja_horaria ():
    '''
    Esta función se encarga de pedirle una franja horaria al usuario.

    Returns
    -------
    El formato de retorno sería: {"hora_min": hora_min
                                  "hora_max": hora_max}
    Raises: No hay. Los errores se manejan internamente

    '''
    
    print ("🕐 Definición de franja horaria deseada (en formato 24hs). Primero, se le va a pedir la hora, y luego, los minutos." 
           "Aclaración: Esta búsqueda no contempla toda la duración del concierto. Es decir, va a utilizarse para buscar conciertos que comiencen dentro de la franja horaria ingresada, pero no considera si el evento termina después del horario indicado como su máximo" )
    
    while True:
        
        try:
            hora_1 = input ("Ingrese la hora mínima.")
            minutos_1 = input ("Ingrese los minutos de la hora mínima")
            
            hora_min = f"{hora_1}:{minutos_1}"
            
            hora_2 = input ("Ingrese la hora máxima")
            minutos_2 = input ("Ingrese los minutos máximos")
            
            hora_max = f"{hora_2}:{minutos_2}"
        
        
            hora_min = pd.to_datetime (hora_min, format = '%H:%M').time()
            hora_max = pd.to_datetime (hora_max, format = '%H:%M').time()
        
            if hora_max < hora_min:
                raise ValueError ("La hora mínima no puede ser después de la hora máxima")
            
            
        except ValueError as e:
            print ("Ingrese el valor nuevamente hasta que sea válido")
        
        else:
            return {"hora_min": hora_min, "hora_max": hora_max}

def pedir_distancia_max():
   
    print ("🗺️ Definición de distancia máxima que esté dispuesto a recorrer.")
    
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
    
   print ("📍 Obtención de la dirección de partida: Va a ingresar la dirección desde donde desee hacer la búsqueda"
          "Este dato será utilizado para calcular las distancias con los eventos y determinar si están dentro del rango solicitado")
   while True: 
        direccion_usuario= input("Ingrese su dirección de partida: ")
        if direccion_usuario.strip()=="":
           print("El ingreso de la dirección no puede estar vacío. Porfavor, vuelva a ingresar su ubicación de partida")
        else: 
            geolocalizador= Nominatim(user_agent= "concertmatch") ##Crea el objeto que se conecta con OpenStreetMap para buscar direcciones.
            ubicacion_usuario= geolocalizador.geocode(direccion_usuario) ##Devuelve latitud y longitud. si la direccion no existe devuelve None.
            if ubicacion_usuario is None: 
                print("La dirección no existe") ## y vuelve al while
            else: 
                latitud_usuario= ubicacion_usuario.latitude
                longitud_usuario= ubicacion_usuario.longitude
                break
   lista_distancias= calcular_distancias(df, latitud_usuario, longitud_usuario) #se llama a funcion que devuelve lista de distancias
   df["distancias"]=lista_distancias #agrega una columna de "distancias" cuyos valores es la lista que devolvió la función calcular_distancias
   
   return df
    

def calcular_distancias(df, latitud_usuario, longitud_usuario):
    lista_distancias = []
    
    for i in df.index:
        latitud_evento = df.loc[i, "latitud"]
        longitud_evento = df.loc[i, "longitud"]
        distancia = geodesic((latitud_usuario, longitud_usuario), (latitud_evento, longitud_evento)).kilometers
        lista_distancias.append(distancia)
    
    return lista_distancias
                
#las funciones pedir_ubicacion_partida, calcular_distancias y pedir_distancia_max no estan completas. Tenemos que ver cómo se comunican entre sí y con las funciones de filtrado.

def pedir_lugar_para_sentarse():
    '''
    Descripción: Solicita una preferencia con respuesta si/no para la categoría "Lugar para sentarse"

    Returns
    -------
    quiere_asientos : bool (True = "Si", False = "No").

    '''
    print ("🪑 Disponibilidad de asientos")
    
    quiere_asientos = hacer_pregunta_si_no("¿Le resulta crucial en su elección que el evento tenga lugar para sentarse ? (si/no): ")
    return quiere_asientos

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
        Condición válida para la categoría solicitada.

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

        return pedir_distancia_max(df_filtrado)

    elif categoria == "lugar para sentarse":

        return pedir_lugar_para_sentarse()
