from Equipo import Equipo 
from NumberGenerator import CongruencialLineal

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
semilla = 42

generadorUniforme = CongruencialLineal(a, c, m, semilla)

def generar_numero_uniforme(min_value, max_value):
    return min_value + (max_value-min_value) * generadorUniforme.generate_number()

class Juego:
    
    def __init__(self, equipoa, equipob):
        self.equipoa = equipoa
        self.equipob = equipob
        self.ronda = 1

    def obtener_equipo_ganador(self):
        puntaje_equipo_a = self.equipoa.obtenerPuntajeTotalEquipo()
        puntaje_equipo_b = self.equipob.obtenerPuntajeTotalEquipo()
        return self.equipoa if puntaje_equipo_a > puntaje_equipo_b else self.equipob if puntaje_equipo_a < puntaje_equipo_b else None
    
    #def obtener_ganador_individual(self):

    def cambiar_suerte_equipo(self, equipo):
        for jugador in equipo.jugadores:
            jugador.suerte = generar_numero_uniforme(min_value, max_value)

    def cambiar_suerte(self):
        self.cambiar_suerte_equipo(self.equipoa)
        self.cambiar_suerte_equipo(self.equipob)