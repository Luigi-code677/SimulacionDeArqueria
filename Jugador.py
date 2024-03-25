import numpy as np

class Jugador:
    def __init__(self, nombre, genero, suerte, resistencia, experiencia):
        self.nombre = nombre
        self.genero = genero
        self.suerte = suerte
        self.resistencia = resistencia
        self.resistencia_total = resistencia
        self.experiencia = experiencia
        #self.puntajes_rondas = np.zeros(shape=10)
        self.rondas = []

    def obtener_total_puntaje(self):
        return self.puntajes_rondas.sum()
    

    