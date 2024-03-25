from Lanzamiento import Lanzamiento
from NumberGenerator import CongruencialLineal

generador = CongruencialLineal(40)


def simular_puntaje(genero):
    numero = generador.generate_number()
    puntaje = 0
    if genero == "Hombre":
        if numero <= 0.07:
            puntaje = 0
        elif 0.07 < numero <= 0.47:
            puntaje = 8
        elif 0.47 < numero <= 0.80:
            puntaje = 9
        else:
            puntaje = 10
    else:
        if numero <= 0.05:
            puntaje = 0
        elif 0.05 < numero <= 0.32:
            puntaje = 8
        elif 0.32 < numero <= 0.70:
            puntaje = 9
        else:
            puntaje = 10
    return puntaje


def realizar_lanzamiento(tipo, puntaje, lanzamientos):
    lanzamiento = Lanzamiento(tipo, puntaje)
    lanzamientos.append(lanzamiento)


class Jugador:
    def __init__(self, nombre, genero, suerte, resistencia, experiencia):
        self.nombre = nombre
        self.genero = genero
        self.suerte = suerte
        self.resistencia = resistencia
        self.resistencia_total = resistencia
        self.experiencia = experiencia
        self.rondas = []

    def obtener_puntaje_ronda_equipo(self, numero_ronda):
        ronda = self.rondas[numero_ronda - 1]
        puntaje = 0
        for lanzamiento in ronda:
            puntaje += lanzamiento.puntaje if lanzamiento.tipo == "Normal" or lanzamiento.tipo == "Equipo" else 0
        return puntaje

    def obtener_puntaje_ronda_individual(self, numero_ronda):
        ronda = self.rondas[numero_ronda - 1]
        puntaje = 0
        for lanzamiento in ronda:
            puntaje += lanzamiento.puntaje if lanzamiento.tipo == "Normal" or lanzamiento.tipo == "Individual" else 0
        return puntaje

    def obtener_puntaje_total_equipo(self):
        puntaje = 0
        for i in range(len(self.rondas)):
            puntaje += self.obtener_puntaje_ronda_equipo(i)
        return puntaje

    def obtener_puntaje_total_individual(self):
        puntaje = 0
        for i in range(len(self.rondas)):
            puntaje += self.obtener_puntaje_ronda_individual(i)
        return puntaje

    def simular_ronda(self):
        resistencia_actual = self.resistencia
        lanzamientos = []
        while self.resistencia >= 5:
            realizar_lanzamiento("Normal", simular_puntaje(self.genero), lanzamientos)
            self.resistencia -= 5
        self.recuperar_puntos(resistencia_actual)
        self.rondas.append(lanzamientos)

    def recuperar_puntos(self, resistencia_anterior):
        numero = generador.generate_number()
        puntos = 2 if numero <= 0.5 else 1
        self.resistencia = resistencia_anterior - puntos