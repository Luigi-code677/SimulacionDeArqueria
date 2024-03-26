import time
import Equipo
import NumberGenerator
from Jugador import Jugador

min_value = 1
max_value = 3
media = 35
desv_estandar = 10
experiencia = 10
cantidad_jugadores = 5

#Cambia el valor de suerte para cada jugador en un equipo utilizando un generador de números aleatorios.
def cambiar_suerte_equipo(equipo, generador):
    for jugador in equipo.jugadores:
        suerte = NumberGenerator.generar_numero_uniforme(min_value, max_value, generador)
        jugador.suerte = suerte

#Calcula el puntaje total de un equipo, incluyendo todas sus rondas
def puntajes_total_equipo(equipo):
    return equipo.obtener_puntaje_total_equipo()


class Juego:
    #Se inicializa el metodo juego.
    def __init__(self, equipoa: Equipo, equipob: Equipo, generador):
        self.equipoa: Equipo = equipoa
        self.equipob: Equipo = equipob
        self.ganadores_ronda: [Jugador] = []
        self.equipo_ganador_ronda: [Equipo] = []
        self.generador = generador

    #Se obtiene el ganador del juego.
    def obtener_equipo_ganador(self) -> Equipo:
        puntaje_equipo_a = self.equipoa.obtener_puntaje_total_equipo()
        puntaje_equipo_b = self.equipob.obtener_puntaje_total_equipo()
        equipo_ganador = self.equipoa if puntaje_equipo_a > puntaje_equipo_b else self.equipob \
            if puntaje_equipo_a < puntaje_equipo_b else None
        return equipo_ganador
    
    #Se obtiene el perdedor del juego.
    def obtener_equipo_perdedor(self) -> Equipo:
        puntaje_equipo_a = self.equipoa.obtener_puntaje_total_equipo()
        puntaje_equipo_b = self.equipob.obtener_puntaje_total_equipo()
        equipo_perdedor = self.equipoa if puntaje_equipo_a < puntaje_equipo_b else self.equipob \
            if puntaje_equipo_a > puntaje_equipo_b else None
        return equipo_perdedor

    #Se obtiene el ganador de la ronda grupal.
    def ganador_ronda_grupal(self, ronda) -> Equipo:
        puntaje_equipo_a = self.equipoa.obtener_puntaje_ronda_equipo(ronda)
        puntaje_equipo_b = self.equipob.obtener_puntaje_ronda_equipo(ronda)
        return self.equipoa if puntaje_equipo_a > puntaje_equipo_b else self.equipob if (puntaje_equipo_a <
                                                                                         puntaje_equipo_b) else None
    

    #Se cambia la suerte de ambos equipos.
    def cambiar_suerte(self):
        cambiar_suerte_equipo(self.equipoa, self.generador)
        cambiar_suerte_equipo(self.equipob, self.generador)


    #Se obtiene el jugador mas suertudo de un juego.
    def jugador_mas_suertudo_juego(self):
        suertudo = None
        contador_suerte = 0
        jugadores = []
        jugadores.extend(self.equipoa.jugadores)
        jugadores.extend(self.equipob.jugadores)
        for jugador in jugadores:
            if jugador.contador_suerte > contador_suerte:
                contador_suerte = jugador.contador_suerte
                suertudo = jugador
        return suertudo
    
    #Se obtiene el jugador mas experimentado de un juego.
    def jugador_mas_experiencia_juego(self):
        experto = None
        experiencia_jugador = 0
        jugadores = []
        jugadores.extend(self.equipoa.jugadores)
        jugadores.extend(self.equipob.jugadores)
        for jugador in jugadores:
            if jugador.experiencia > experiencia_jugador:
                experiencia_jugador = jugador.experiencia
                experto = jugador
        return experto
    

    #Se obtiene un diccionario con las victorias por genero en un juego.
    def victorias_por_generos(self):
        contadores_genero = {"Hombre": 0, "Mujer": 0}
        for jugador in self.ganadores_ronda:
            if jugador.genero in contadores_genero:
                contadores_genero[jugador.genero] += 1
        return contadores_genero
    
    #Se actualizan las estadisticas de un jugador.
    def actualizar_evolucion(self):
        self.equipoa.actualizar_evolucion_jugador()
        self.equipob.actualizar_evolucion_jugador()

    #Se simula un juego. 
    def simular_juego(self):
        for i in range(10):
            self.cambiar_suerte()
            self.equipoa.simular_ronda()
            self.equipob.simular_ronda()

            # Jugador Ganador de la ronda
            jugadores_total = []
            jugadores_total.extend(self.equipoa.jugadores)
            jugadores_total.extend(self.equipob.jugadores)
            ganador = Equipo.ganador_ronda_individual(jugadores_total, i)
            ganador.experiencia += 3
            self.ganadores_ronda.append(ganador)

            # Ganador ronda grupal
            equipo = self.ganador_ronda_grupal(i)
            self.equipo_ganador_ronda.append(equipo)
