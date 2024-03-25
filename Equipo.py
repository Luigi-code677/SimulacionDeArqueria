from Jugador import Jugador

class Equipo:

    def __init__(self, nombre, jugadores):
        self.nombre = nombre
        self.jugadores = jugadores

        
    def obtenerPuntajeRondaEquipo(self, numero_ronda):
        puntaje = 0
        for jugador in self.jugadores:
            puntaje += jugador.puntajes_rondas[numero_ronda-1]
        return puntaje
    
    def obtener_puntaje_total_equipo(self):
        puntaje = 0
        for i in range(10):
            puntaje += self.obtenerPuntajeRondaEquipo(i+1)
        return puntaje
    
    def jugador_mas_puntaje(self):
        maximo_puntaje = 0
        for jugador in self.jugadores:
            puntaje = jugador.obtener_total_puntaje()
            maximo_puntaje = puntaje if puntaje > maximo_puntaje else maximo_puntaje



