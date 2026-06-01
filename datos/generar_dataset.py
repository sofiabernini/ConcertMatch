# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 14:54:18 2026

@author: sofia
"""

# Código que genera el Dataset con el que vamos a trabajar

import csv
import random
from datetime import datetime, timedelta

# 1. Base de datos de predios reales en Buenos Aires (¡Ahora con Huracán incluido!)
PREDIOS_BA = {
    "Estadio River Plate": {
        "direccion": "Av. Figueroa Alcorta 7597, Núñez, CABA",
        "movilidad": "True",
        "asientos": "True",
        "ticketera": "https://www.allaccess.com.ar"
    },
    "Movistar Arena": {
        "direccion": "Humboldt 450, Villa Crespo, CABA",
        "movilidad": "True",
        "asientos": "True",
        "ticketera": "https://www.movistararena.com.ar"
    },
    "Estadio Vélez Sarsfield": {
        "direccion": "Av. Juan B. Justo 9200, Liniers, CABA",
        "movilidad": "True",
        "asientos": "True",
        "ticketera": "https://www.entradauno.com"
    },
    "Estadio Huracán": {
        "direccion": "Av. Amancio Alcorta 2544, Parque Patricios, CABA",
        "movilidad": "True",
        "asientos": "True",
        "ticketera": "https://www.ticketek.com.ar"
    },
    "Teatro Colón": {
        "direccion": "Cerrito 628, San Nicolás, CABA",
        "movilidad": "True",
        "asientos": "True",
        "ticketera": "https://www.tuentrada.com"
    },
    "Luna Park": {
        "direccion": "Av. Eduardo Madero 420, San Nicolás, CABA",
        "movilidad": "True",
        "asientos": "True",
        "ticketera": "https://www.ticketportal.com.ar"
    },
    "La Trastienda": {
        "direccion": "Balcarce 460, San Telmo, CABA",
        "movilidad": "True",
        "asientos": "False",
        "ticketera": "https://www.tuentrada.com"
    },
    "Centro Cultural Kirchner": {
        "direccion": "Sarmiento 151, San Nicolás, CABA",
        "movilidad": "True",
        "asientos": "True",
        "ticketera": "https://www.cck.gob.ar"
    },
    "Centro Cultural Recoleta": {
        "direccion": "Junín 1930, Recoleta, CABA",
        "movilidad": "True",
        "asientos": "False",
        "ticketera": "https://www.buenosaires.gob.ar/centroculturalrecoleta"
    },
    "Complejo Art Media": {
        "direccion": "Av. Corrientes 6271, Chacarita, CABA",
        "movilidad": "True",
        "asientos": "False",
        "ticketera": "https://www.passline.com"
    },
    "Estadio Obras Sanitarias": {
        "direccion": "Av. del Libertador 7395, Núñez, CABA",
        "movilidad": "True",
        "asientos": "True",
        "ticketera": "https://www.tuentrada.com"
    }
}

# 2. Artistas en cartelera / escena actual de Buenos Aires
ARTISTAS_BA = [
    ("Oasis", "Rock Británico", ["Estadio River Plate", "Estadio Vélez Sarsfield"]),
    ("Shakira", "Pop Latino", ["Estadio River Plate", "Movistar Arena"]),
    ("Charly García", "Rock Nacional", ["Movistar Arena", "Teatro Colón", "Luna Park"]),
    ("Duki", "Trap", ["Estadio River Plate", "Estadio Vélez Sarsfield", "Movistar Arena"]),
    ("Bizarrap", "EDM/Urbano", ["Movistar Arena", "Complejo Art Media"]),
    ("Divididos", "Rock Nacional", ["Estadio Vélez Sarsfield", "Luna Park", "Estadio Obras Sanitarias"]),
    ("Wos", "Rap/Rock", ["Movistar Arena", "Estadio Obras Sanitarias"]),
    ("Fito Páez", "Rock Nacional", ["Movistar Arena", "Teatro Colón"]),
    ("Babasonicos", "Rock Alternativo", ["Movistar Arena", "Luna Park", "La Trastienda"]),
    ("Tini", "Pop", ["Movistar Arena", "Luna Park"]),
    ("Los Fabulosos Cadillacs", "Ska/Rock", ["Estadio River Plate", "Movistar Arena"]),
    ("Dillom", "Alternativo/Urbano", ["Luna Park", "Complejo Art Media"]),
    ("Miranda!", "Electro Pop", ["Movistar Arena", "Luna Park", "La Trastienda"]),
    ("Nicki Nicole", "Urbano", ["Movistar Arena", "Luna Park"]),
    ("Conociendo Rusia", "Indie Rock", ["Movistar Arena", "Complejo Art Media", "La Trastienda"]),
    ("El Kuelgue", "Indie/Fusión", ["Movistar Arena", "Complejo Art Media"]),
    ("La Renga", "Hard Rock", ["Estadio Huracán", "Estadio Obras Sanitarias"]),
    ("Orquesta Filarmónica de Buenos Aires", "Clásica", ["Teatro Colón", "Centro Cultural Kirchner"]),
    ("Ciclo de Jazz y Blues", "Jazz", ["La Trastienda", "Centro Cultural Kirchner"]),
    ("Bandas de Indie Emergente", "Indie", ["Centro Cultural Recoleta", "Complejo Art Media"]),
    ("Sinfónica Nacional", "Clásica", ["Centro Cultural Kirchner"]),
    ("Festival de Folclore Urbano", "Folclore", ["Centro Cultural Kirchner", "Centro Cultural Recoleta"])
]

FECHA_BASE = datetime.now()

# Creación del archivo CSV
with open('conciertos_buenos_aires.csv', mode='w', newline='', encoding='utf-8') as archivo:
    escritor = csv.writer(archivo)
    
    # Encabezados
    escritor.writerow([
        "artista_banda", "genero", "precio", "fecha", "hora", 
        "direccion", "lugar", "acceso_movilidad_reducida", 
        "cuenta_con_asientos", "ticketera_link", "agotado"
    ])
    
    for _ in range(1000):
        artista, genero, predios_disponibles = random.choice(ARTISTAS_BA)
        lugar = random.choice(predios_disponibles)
        info_lugar = PREDIOS_BA[lugar]
        
        # Lógica de precios
        if "Centro Cultural" in lugar:
            precio = 0
        else:
            if "River" in lugar:
                precio = random.randint(45000, 150000)
            elif "Movistar" in lugar or "Vélez" in lugar or "Huracán" in lugar:
                precio = random.randint(35000, 110000)
            elif "Obras" in lugar or "Luna" in lugar:
                precio = random.randint(25000, 75000)
            else:
                precio = random.randint(15000, 45000)
        
        # Fecha aleatoria en los próximos 6 meses
        dias_a_sumar = random.randint(1, 180)
        fecha_evento = (FECHA_BASE + timedelta(days=dias_a_sumar)).strftime("%Y-%m-%d")
        hora = random.choice(["20:00", "20:30", "21:00", "19:00"])
        
        # Agotado (True/False)
        agotado = str(random.choice([True, False]))
        
        escritor.writerow([
            artista, genero, precio, fecha_evento, hora,
            info_lugar["direccion"], lugar, info_lugar["movilidad"],
            info_lugar["asientos"], info_lugar["ticketera"], agotado
        ])