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


if __name__ == '__main__':
    lucho = Jugador("Lucho", "Hombre", 1.3, 25, 10)
    david = Jugador("David", "Hombre", 1.4, 30, 10)
    carla = Jugador("Carla", "Mujer", 1.2, 35, 10)
    nicol = Jugador("Nick", "Mujer", 2.3, 25, 10)
    edwin = Jugador("Edi", "Hombre", 2.1, 30, 10)
    alfredo = Jugador("Alfred", "Hombre", 2.5, 35, 10)
    equi_a = Equipo("A", [lucho, david, carla])
    equi_b = Equipo("B", [nicol, edwin, alfredo])

    equi_a.simular_ronda()
    equi_a.simular_ronda()
    equi_a.simular_ronda()
    equi_a.simular_ronda()
    equi_a.simular_ronda()
    equi_b.simular_ronda()
    equi_b.simular_ronda()
    equi_b.simular_ronda()
    equi_b.simular_ronda()
    equi_b.simular_ronda()

    print(equi_a.obtener_puntaje_ronda_equipo(1))
    print(equi_b.obtener_puntaje_ronda_equipo(1))
    print(equi_a.obtener_puntaje_ronda_equipo(2))
    print(equi_b.obtener_puntaje_ronda_equipo(2))
    print(equi_a.obtener_puntaje_ronda_equipo(3))
    print(equi_b.obtener_puntaje_ronda_equipo(3))
    print(equi_a.obtener_puntaje_ronda_equipo(4))
    print(equi_b.obtener_puntaje_ronda_equipo(4))
    print(equi_a.obtener_puntaje_ronda_equipo(5))
    print(equi_b.obtener_puntaje_ronda_equipo(5))
