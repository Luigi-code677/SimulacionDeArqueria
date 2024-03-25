import pandas as pd
from NumberGenerator import CongruencialLineal
from Jugador import Jugador
import NumberGenerator

min_value = 1
max_value = 3
media = 35
desv_estandar = 10
experiencia = 10
semilla = 42
generador_uniforme = CongruencialLineal(semilla)  # Ni con distribucion normal
generador_normal = CongruencialLineal(semilla + 10)  # Ni con distribucion uniforme
generador_ri = CongruencialLineal(semilla - 5)  # Ri [0,1]


def generar_atributos_jugador():
    # Generar suerte con distribución uniforme entre 1 y 3
    suerte = NumberGenerator.generar_numero_uniforme(min_value, max_value, generador_uniforme)
    # Generar resistencia con distribución normal (media 35, desviación estándar 10)
    resistencia = int(NumberGenerator.generar_numero_normal(media, desv_estandar, generador_normal))
    return suerte, resistencia


def generar_jugador(genero, num_jugador, equipo):
    suerte, resistencia = generar_atributos_jugador()
    nombre = f"{equipo} {num_jugador}"
    return Jugador(nombre, genero, suerte, resistencia, experiencia)


def generar_equipo(nombre_equipo):
    equipo = []
    genero = ""
    numeros = NumberGenerator.generar_n_numeros(5, generador_ri)
    for i in range(len(numeros)):
        if numeros[i] >= 0.5:
            genero = "Hombre"
        else:
            genero = "Mujer"
        equipo.append(generar_jugador(genero, i + 1, nombre_equipo))
    return equipo


equipoa = generar_equipo("Equipo A")
equipob = generar_equipo("Equipo B")

if __name__ == '__main__':
    for jugador in equipoa:
        print(
            f"Nombre: {jugador.nombre}, Género: {jugador.genero}, Suerte: {jugador.suerte}, Resistencia: {jugador.resistencia}, Experiencia: {jugador.experiencia}")

    for jugador in equipob:
        print(
            f"Nombre: {jugador.nombre}, Género: {jugador.genero}, Suerte: {jugador.suerte}, Resistencia: {jugador.resistencia}, Experiencia: {jugador.experiencia}")
