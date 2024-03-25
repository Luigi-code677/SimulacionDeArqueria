# import pandas as pd
# from NumberGenerator import CongruencialLineal
# from scipy.stats import norm
# import time
# from Jugador import Jugador
#
#
# k = 47794729  # Valor k
# c = 11  # Valor c
# g = 20  # Valor g
# min_value = 1
# max_value = 3
# media = 35
# desv_estandar = 10
# experiencia = 10
# cantidad_jugadores = 5
#
# a = 1 + 2 * k
# m = 2 ** g
# semilla = 42 #int(time.time() * 1000000) % m
#
# generadorUniforme = CongruencialLineal(a, c, m, semilla)
# generadorNormal = CongruencialLineal(a, c, m, semilla)

# def generar_n_numeros(cantidad):
#     global semilla
#     ri_values = [generadorUniforme.generate_number() for _ in range(cantidad)]
#     semilla = semilla + 5
#     return ri_values
#
# def generar_numero_uniforme(min_value, max_value):
#     return min_value + (max_value-min_value) * generadorUniforme.generate_number()
#
# def generar_numero_normal(media, desv_estandar):
#     return norm.ppf(generadorNormal.generate_number(), media, desv_estandar)
#
# def generar_atributos_jugador():
#     # Generar suerte con distribución uniforme entre 1 y 3
#     suerte = generar_numero_uniforme(min_value, max_value)
#     # Generar resistencia con distribución normal (media 35, desviación estándar 10)
#     resistencia = int(generar_numero_normal(media, desv_estandar))
#     return suerte, resistencia
#
# #generar_atributos_jugador()
#
#
#
# def generar_jugador(genero, num_jugador, equipo):
#     suerte, resistencia = generar_atributos_jugador()
#     nombre = f"{equipo} {num_jugador}"
#     return Jugador(nombre, genero, suerte, resistencia, experiencia)
#
# def generar_equipo(nombre_equipo):
#     equipo = []
#     genero = ""
#     numeros = generar_n_numeros(5)
#     for i in range (len(numeros)):
#         if numeros[i] >= 0.5:
#             genero = "Hombre"
#         else:
#             genero = "Mujer"
#         equipo.append(generar_jugador(genero, i+1, nombre_equipo))
#     return equipo
#
# equipoa = generar_equipo("Equipo A")
#
# equipob = generar_equipo("Equipo B")
#
# for jugador in equipoa:
#     print(f"Nombre: {jugador.nombre}, Género: {jugador.genero}, Suerte: {jugador.suerte}, Resistencia: {jugador.resistencia}, Experiencia: {jugador.experiencia}")
#
# for jugador in equipob:
#     print(f"Nombre: {jugador.nombre}, Género: {jugador.genero}, Suerte: {jugador.suerte}, Resistencia: {jugador.resistencia}, Experiencia: {jugador.experiencia}")

precision = {
    "Central": {"Mujeres": 0.30, "Hombres": 0.20, "Puntaje": 10},
    "Intermedia": {"Mujeres": 0.38, "Hombres": 0.33, "Puntaje": 9},
    "Exterior": {"Mujeres": 0.27, "Hombres": 0.40, "Puntaje": 8},
    "Error": {"Mujeres": 0.05, "Hombres": 0.07, "Puntaje": 0}
}

# def simular_lanzamiento(jugador):
#     resistencia_actual = jugador.resistencia
#     while jugador.resistencia >= 5:
#         jugador.puntaje_ronda += simular_puntaje(jugador.genero)
#         resistencia_actual -= 5
#     recuperar_puntos(resistencia_actual, jugador)
#
#
# def simular_puntaje(genero):
#     numero = generar_n_numeros(1)
#     puntaje = 0
#     if genero == "Hombre":
#         if numero[0] <= 0.07:
#             puntaje = 0
#         elif 0.07 < numero[0] <= 0.47:
#             puntaje = 8
#         elif 0.47 < numero[0] <= 0.80:
#             puntaje = 9
#         else:
#             puntaje = 10
#     else:
#         if numero[0] <= 0.05:
#             puntaje = 0
#         elif 0.05 < numero[0] <= 0.32:
#             puntaje = 8
#         elif 0.32 < numero[0] <= 0.70:
#             puntaje = 9
#         else:
#             puntaje = 10
#     return puntaje
#
#
# def recuperar_puntos(resistencia_anterior, jugador):
#     numero = int(generar_numero_uniforme(1,2))
#     jugador.resistencia = resistencia_anterior - numero

def obtener_jugador_mas_suerte(equipo):
    mas_suerte = 0
    for jugador in equipo:
        if jugador.suerte > mas_suerte:
            mas_suerte = jugador.suerte
            jugador_mas_suerte = jugador
    return jugador_mas_suerte


def simularRonda(equipoa, equipob):
    puntaje_equipo_a = 0
    puntaje_equipo_b = 0

    
    jugador_mas_suerte_a = obtener_jugador_mas_suerte(equipoa)
    jugador_mas_suerte_b = obtener_jugador_mas_suerte(equipob)
    

    for jugador in equipoa:
        simular_lanzamiento(jugador)
        recuperar_puntos(jugador.resistencia_total, jugador)
        puntaje_equipo_a += jugador.puntaje_ronda
    
    for jugador in equipob:
        simular_lanzamiento(jugador)
        recuperar_puntos(jugador.resistencia_total, jugador)

        puntaje_equipo_b += jugador.puntaje_ronda
    
    

    print("Puntaje equipo a: ", puntaje_equipo_a, " Puntaje equipo b: ", puntaje_equipo_b )

simularRonda(equipoa, equipob)



    
    

    






    
