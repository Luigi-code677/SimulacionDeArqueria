from Jugador import Jugador


def ganador_ronda_indivicual(equipo_1, equipo_2, ronda):
    puntaje_max = 0
    ganador = None
    jugadores_total = [equipo_1.jugadores, equipo_2.jugadores]
    for jugador in jugadores_total:
        puntaje_jugador = jugador.obtener_puntaje_ronda_individual(ronda)
        if puntaje_jugador > puntaje_max:
            puntaje_max = puntaje_jugador
            ganador = jugador
    return ganador


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
            puntaje += self.obtener_puntaje_ronda_equipo(i + 1)
        return puntaje

    def simular_ronda(self):
        for jugador in self.jugadores:
            jugador.simular_ronda()


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


