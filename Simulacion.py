import pandas as pd
from NumberGenerator import CongruencialLineal
from scipy.stats import norm 
from Jugador import Jugador



min_value = 1
max_value = 3
media = 35
desv_estandar = 10
experiencia = 10
cantidad_jugadores = 5



generadorUniforme = CongruencialLineal(a, c, m, semilla)
generadorNormal = CongruencialLineal(a, c, m, semilla)

def generar_n_numeros(cantidad):
    global semilla
    ri_values = [generadorUniforme.generate_number() for _ in range(cantidad)]
    semilla = semilla + 5 
    return ri_values

def generar_numero_uniforme(min_value, max_value):
    return min_value + (max_value-min_value) * generadorUniforme.generate_number()

def generar_numero_normal(media, desv_estandar):
    return norm.ppf(generadorNormal.generate_number(), media, desv_estandar)
    
def generar_atributos_jugador():
    # Generar suerte con distribución uniforme entre 1 y 3
    suerte = generar_numero_uniforme(min_value, max_value)
    # Generar resistencia con distribución normal (media 35, desviación estándar 10)
    resistencia = int(generar_numero_normal(media, desv_estandar))
    return suerte, resistencia


def generar_jugador(genero, num_jugador, equipo):
    suerte, resistencia = generar_atributos_jugador()
    nombre = f"{equipo} {num_jugador}"
    return Jugador(nombre, genero, suerte, resistencia, experiencia)

def generar_equipo(nombre_equipo):
    equipo = []
    genero = ""
    numeros = generar_n_numeros(5)
    for i in range (len(numeros)):
        if numeros[i] >= 0.5:
            genero = "Hombre"
        else:
            genero = "Mujer"
        equipo.append(generar_jugador(genero, i+1, nombre_equipo))
    return equipo
    
equipoa = generar_equipo("Equipo A")

equipob = generar_equipo("Equipo B")

for jugador in equipoa:
    print(f"Nombre: {jugador.nombre}, Género: {jugador.genero}, Suerte: {jugador.suerte}, Resistencia: {jugador.resistencia}, Experiencia: {jugador.experiencia}")

for jugador in equipob:
    print(f"Nombre: {jugador.nombre}, Género: {jugador.genero}, Suerte: {jugador.suerte}, Resistencia: {jugador.resistencia}, Experiencia: {jugador.experiencia}")
