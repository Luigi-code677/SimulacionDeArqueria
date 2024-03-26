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
        self.experiencia_inicial = experiencia
        self.experiencia = experiencia
        self.rondas = []
        self.rondas_extra = []
        self.contador_suerte = 0
        self.contador_experiencia_resistencia = 0

    def obtener_puntaje_ronda_equipo(self, numero_ronda):
        ronda = self.rondas[numero_ronda]
        puntaje = 0
        for lanzamiento in ronda:
            puntaje += lanzamiento.puntaje if lanzamiento.tipo == "Normal" or lanzamiento.tipo == "Equipo" else 0
        return puntaje

    def obtener_puntaje_ronda_individual(self, numero_ronda):
        ronda = self.rondas[numero_ronda]
        puntaje = 0
        for lanzamiento in ronda:
            puntaje += lanzamiento.puntaje if lanzamiento.tipo == "Normal" or lanzamiento.tipo == "Individual" else 0
        return puntaje

    def obtener_puntaje_total_equipo(self):
        puntaje = 0
        for i in range(len(self.rondas)):
            puntaje += self.obtener_puntaje_ronda_equipo(i+1)
        return puntaje

    def obtener_puntaje_total_individual(self):
        puntaje = 0
        for i in range(len(self.rondas)):
            puntaje += self.obtener_puntaje_ronda_individual(i)
        return puntaje

    def simular_ronda(self) -> int:
        resistencia_actual = self.resistencia
        lanzamientos = []
        while self.resistencia >= 5:
            realizar_lanzamiento("Normal", simular_puntaje(self.genero), lanzamientos)
            if self.experiencia >= self.experiencia_inicial + 9 and self.contador_experiencia_resistencia < 2:
                self.resistencia -= 1
                self.contador_experiencia_resistencia += 1
            else:
                self.resistencia -= 5
        self.recuperar_puntos(resistencia_actual)
        self.rondas.append(lanzamientos)
        return len(self.rondas)-1

    def lanzamiento_extra_equipo(self, ronda):
        realizar_lanzamiento("Equipo", simular_puntaje(self.genero), self.rondas[ronda])
        self.contador_suerte += 1

    def lanzamiento_extra_individual(self, ronda):
        realizar_lanzamiento("Individual", simular_puntaje(self.genero), self.rondas[ronda])

    def recuperar_puntos(self, resistencia_anterior):
        numero = generador.generate_number()
        puntos = 2 if numero <= 0.5 else 1
        self.resistencia = resistencia_anterior - puntos
