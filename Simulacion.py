import time

from Equipo import Equipo
from Juego import Juego
import Juego as Jg
from NumberGenerator import CongruencialLineal
from Jugador import Jugador
import NumberGenerator

min_value = 1
max_value = 3
media = 35
desv_estandar = 10
experiencia = 10
# semilla = int(time.time())
semilla = 42
generador_ri = CongruencialLineal(semilla - 5)  # Ri [0,1]


def generar_atributos_jugador():
    # Generar suerte con distribución uniforme entre 1 y 3
    suerte = NumberGenerator.generar_numero_uniforme(min_value, max_value, generador_ri)
    # Generar resistencia con distribución normal (media 35, desviación estándar 10)
    resistencia = int(NumberGenerator.generar_numero_normal(media, desv_estandar, generador_ri))
    return suerte, resistencia


def generar_jugador(genero, num_jugador, equipo):
    suerte, resistencia = generar_atributos_jugador()
    nombre = f"{equipo} {num_jugador}"
    return Jugador(nombre, genero, suerte, resistencia, experiencia, generador_ri)


def generar_equipo(nombre_equipo):
    jugadores = []
    genero = ""
    numeros = NumberGenerator.generar_n_numeros(5, generador_ri)
    for i in range(len(numeros)):
        if numeros[i] >= 0.5:
            genero = "Hombre"
        else:
            genero = "Mujer"
        jugadores.append(generar_jugador(genero, i + 1, nombre_equipo))
    return Equipo(nombre_equipo, jugadores)


equipoa = generar_equipo("Equipo A")
equipob = generar_equipo("Equipo B")


def informacion_jugador(jugador_aux):
    return Jugador(jugador_aux.nombre, jugador_aux.genero, jugador_aux.suerte,
                   jugador_aux.resistencia, jugador_aux.experiencia, generador_ri)


def simular_juegos(cantidad):
    print("semilla", semilla)
    jugadores_suertudos = []
    jugadores_expertos = []
    equipo_ganadores = []
    puntajes_equipo = []
    victorias_por_generos = []
    for i in range(cantidad):
        juego = Juego(equipoa, equipob, generador_ri)
        juego.simular_juego()

        jugadores_suertudos.append(informacion_jugador(juego.jugador_mas_suertudo_juego()))
        jugadores_expertos.append(informacion_jugador(juego.jugador_mas_experiencia_juego()))

        equipo_ganador = juego.obtener_equipo_ganador()
        equipo_ganadores.append(equipo_ganador)
        if equipo_ganador is not None:
            puntajes_equipo.append(Jg.puntajes_total_equipo(equipo_ganador))
        else:
            puntajes_equipo.append(0)

        victorias_por_generos.append(juego.victorias_por_generos())

        juego.actualizar_evolucion()

    for i in range(cantidad):
        print("Juego #", i + 1)
        print("Suertudo", jugadores_suertudos[i].nombre)
        # print("Experto", jugadores_expertos[i].nombre, jugadores_expertos[i].experiencia)
        # print("Equipo ganador", equipo_ganadores[i].nombre or "Empate")
        # print("Puntaje", puntajes_equipo[i])
        # print("Victorias", victorias_por_generos[i])


if __name__ == '__main__':
    for jugador in equipoa.jugadores:
        print(
            f"Nombre: {jugador.nombre}, Género: {jugador.genero}, Suerte: {jugador.suerte}, "
            f"Resistencia: {jugador.resistencia}, Experiencia: {jugador.experiencia}")

    for jugador in equipob.jugadores:
        print(
            f"Nombre: {jugador.nombre}, Género: {jugador.genero}, Suerte: {jugador.suerte}, "
            f"Resistencia: {jugador.resistencia}, Experiencia: {jugador.experiencia}")

    simular_juegos(1000)
