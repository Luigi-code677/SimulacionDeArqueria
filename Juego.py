import NumberGenerator
from NumberGenerator import CongruencialLineal

min_value = 1
max_value = 3
media = 35
desv_estandar = 10
experiencia = 10
cantidad_jugadores = 5
semilla = 99


def cambiar_suerte_equipo(equipo):
    global semilla
    generador = CongruencialLineal(semilla)
    for jugador in equipo.jugadores:
        jugador.suerte = NumberGenerator.generar_numero_uniforme(min_value, max_value, generador)


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

    def cambiar_suerte(self):
        cambiar_suerte_equipo(self.equipoa)
        cambiar_suerte_equipo(self.equipob)
