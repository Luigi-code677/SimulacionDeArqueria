import pandas as pd
from NumberGenerator import CongruencialLineal
from scipy.stats import norm 
import time

k = 47794729  # Valor k
c = 11  # Valor c
g = 20  # Valor g
min_value = 1
max_value = 3
media = 35
desv_estandar = 10
experiencia = 10
cantidad_jugadores = 5

a = 1 + 2 * k
m = 2 ** g
semilla = 42 #int(time.time() * 1000000) % m

generador = CongruencialLineal(a, c, m, semilla)

def generar_n_numeros(cantidad):
    ri_values = [generador.generate_number() for _ in range(cantidad)]
    semilla = semilla + 5 
    return ri_values

def generar_numero():
    return generador.generate_number()


def generar_atributos_jugador():
    # Generar suerte con distribución uniforme entre 1 y 3
    suerte = min_value + (max_value-min_value) * generar_numero()

    # Generar resistencia con distribución normal (media 35, desviación estándar 10)
    resistencia = scipy.stats.norm.ppf(generar_numero())

    return suerte, resistencia

generar_atributos_jugador()


class Jugador:
    def __init__(self, nombre, genero, suerte, resistencia, experiencia):
        self.nombre = nombre
        self.genero = genero
        self.suerte = suerte
        self.resistencia = resistencia
        self.experiencia = experiencia
