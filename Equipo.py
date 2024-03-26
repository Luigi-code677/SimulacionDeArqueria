from Jugador import Jugador


def ganador_ronda_individual(jugadores, ronda) -> Jugador:
    puntaje_max = 0
    ganadores = []

    for jugador in jugadores:
        puntaje_jugador = jugador.obtener_puntaje_ronda_individual(ronda)
        if puntaje_jugador > puntaje_max:
            puntaje_max = puntaje_jugador
            ganadores = [jugador]
        elif puntaje_jugador == puntaje_max:
            ganadores.append(jugador)

    if len(ganadores) == 1:
        return ganadores[0]
    else:
        for jugador in ganadores:
            jugador.lanzamiento_extra_individual(ronda)
        return ganador_ronda_individual(ganadores, ronda)


class Equipo:

    def __init__(self, nombre, jugadores):
        self.nombre = nombre
        self.jugadores = jugadores

    def obtener_puntaje_ronda_equipo(self, numero_ronda):
        puntaje = 0
        for jugador in self.jugadores:
            puntaje += jugador.obtener_puntaje_ronda_equipo(numero_ronda)
        return puntaje

    def obtener_puntaje_total_equipo(self):
        puntaje = 0
        for i in range(10):
            puntaje += self.obtener_puntaje_ronda_equipo(i)
        return puntaje

    def jugador_mas_suerte(self) -> Jugador:
        suerte = 0
        suertudo = None
        for jugador in self.jugadores:
            suerte_jugador = jugador.suerte
            if suerte_jugador > suerte:
                suerte = suerte_jugador
                suertudo = jugador
        return suertudo

    def simular_ronda(self):
        suertudo = self.jugador_mas_suerte()
        ronda = 0
        for jugador in self.jugadores:
            ronda = jugador.simular_ronda()
        suertudo.lanzamiento_extra_equipo(ronda)
        suertudo.rondas_extra.append(ronda)
        if len(suertudo.rondas_extra) >= 3:
            ultimos_3_extra = suertudo.rondas_extra[-3:]
            if ultimos_3_extra[0] == ultimos_3_extra[1] - 1 == ultimos_3_extra[2] - 2:
                suertudo.lanzamiento_extra_equipo(ronda)
                suertudo.rondas_extra = []

    def actualizar_evolucion_jugador(self):
        for jugador in self.jugadores:
            jugador.experiencia_inicial = jugador.experiencia
            jugador.resistencia = jugador.resistencia_total
            jugador.rondas = []
            jugador.rondas_extra = []
            jugador.contador_experiencia_resistencia = 0
            jugador.contador_suerte = 0
