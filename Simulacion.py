import time
import pandas as pd
from Equipo import Equipo
from Juego import Juego
import Juego as Jg
from NumberGenerator import CongruencialLineal
from Jugador import Jugador
import NumberGenerator
from collections import Counter

# Definir los parámetros para la generación de números aleatorios
min_value = 1
max_value = 3
media = 35
desv_estandar = 10
experiencia = 10
semilla = int(time.time())
generador_ri = CongruencialLineal(semilla - 5)  # Ri [0,1]


#Función para actualizar la semilla del generador de números aleatorios.
def set_semilla():
    semilla += 5
    generador_ri.xn = semilla

#Función para generar los atributos de suerte y resistencia de un jugador.
def generar_atributos_jugador():
    # Generar suerte con distribución uniforme entre 1 y 3
    suerte = NumberGenerator.generar_numero_uniforme(min_value, max_value, generador_ri)
    # Generar resistencia con distribución normal (media 35, desviación estándar 10)
    resistencia = int(NumberGenerator.generar_numero_normal(media, desv_estandar, generador_ri))
    return suerte, resistencia

#Función para generar un jugador con atributos aleatorios.
def generar_jugador(genero, num_jugador, equipo):
    suerte, resistencia = generar_atributos_jugador()
    nombre = "Jugador"f"{equipo}{num_jugador}"
    return Jugador(nombre, genero, suerte, resistencia, experiencia, generador_ri)

#Función para generar un equipo con jugadores aleatorios.
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

#Generacion de equipos A y B
equipoa = generar_equipo("EquipoA")
equipob = generar_equipo("EquipoB")

#Función para obtener la información de un jugador.
def informacion_jugador(jugador_aux):
    return Jugador(jugador_aux.nombre, jugador_aux.genero, jugador_aux.suerte,
                   jugador_aux.resistencia, jugador_aux.experiencia, generador_ri)

#Función para simular una cantidad especificada de juegos.
def simular_juegos(cantidad): 
    for jugador in equipoa.jugadores:
        print(
            f"Nombre: {jugador.nombre}, Género: {jugador.genero}, Suerte: {jugador.suerte}, "
            f"Resistencia: {jugador.resistencia}, Experiencia: {jugador.experiencia}")

    for jugador in equipob.jugadores:
        print(
            f"Nombre: {jugador.nombre}, Género: {jugador.genero}, Suerte: {jugador.suerte}, "
            f"Resistencia: {jugador.resistencia}, Experiencia: {jugador.experiencia}")
    jugadores_suertudos = []
    jugadores_expertos = []
    equipo_ganadores = []
    equipo_perdedores = []
    puntajes_equipo_ganador = []
    puntajes_equipo_perdedor = []
    victorias_por_generos = []

    # Procesar los resultados de los juegos
    for i in range(cantidad):
        juego = Juego(equipoa, equipob, generador_ri)
        juego.simular_juego()

        jugadores_suertudos.append(informacion_jugador(juego.jugador_mas_suertudo_juego()))
        jugadores_expertos.append(informacion_jugador(juego.jugador_mas_experiencia_juego()))

        equipo_ganador = juego.obtener_equipo_ganador()
        equipo_perdedor = juego.obtener_equipo_perdedor()
        equipo_ganadores.append(equipo_ganador)
        equipo_perdedores.append(equipo_perdedor)
        if equipo_ganador is not None:
            puntajes_equipo_ganador.append(Jg.puntajes_total_equipo(equipo_ganador))
        else:
            puntajes_equipo_ganador.append(0)
        
        if equipo_perdedor is not None:
            puntajes_equipo_perdedor.append(Jg.puntajes_total_equipo(equipo_perdedor))
        else:
            puntajes_equipo_perdedor.append(0)

        victorias_por_generos.append(juego.victorias_por_generos())

        juego.actualizar_evolucion()

    datos_equipo_ganador = []
    datos_equipo_perdedor = []
    datos_jugador_suerte = []
    datos_jugador_experiencia = []
    datos_genero_ganador = []

    for i in range(cantidad):
        juego_actual = i + 1
        equipo_ganador_actual = equipo_ganadores[i].nombre if equipo_ganadores[i] is not None else "Empate"
        puntaje_equipo_ganador_actual = puntajes_equipo_ganador[i]
        equipo_perdedor_actual = equipo_perdedores[i].nombre if equipo_perdedores[i] is not None else "Empate"
        puntaje_equipo_perdedor_actual = puntajes_equipo_perdedor[i]
        jugador_suerte_actual = jugadores_suertudos[i].nombre
        jugador_experiencia_actual = jugadores_expertos[i].nombre
        genero_ganador_actual = "Hombre" if victorias_por_generos[i]["Hombre"] > victorias_por_generos[i]["Mujer"] else "Mujer"

        # Agregar los datos a las listas correspondientes
        datos_equipo_ganador.append((juego_actual, equipo_ganador_actual, puntaje_equipo_ganador_actual))
        datos_equipo_perdedor.append((juego_actual, equipo_perdedor_actual, puntaje_equipo_perdedor_actual))
        datos_jugador_suerte.append((juego_actual, jugador_suerte_actual))
        datos_jugador_experiencia.append((juego_actual, jugador_experiencia_actual))
        datos_genero_ganador.append((juego_actual, genero_ganador_actual))
    
    # Crear DataFrames con los resultados
    df_equipo_ganador = pd.DataFrame(datos_equipo_ganador, columns=["Juego", "Equipo Ganador", "Puntaje"])
    df_equipo_perdedor = pd.DataFrame(datos_equipo_perdedor, columns=["Juego", "Equipo Perdedor", "Puntaje"])
    df_jugador_suerte = pd.DataFrame(datos_jugador_suerte, columns=["Juego", "Jugador con mas suerte"])
    df_jugador_experiencia = pd.DataFrame(datos_jugador_experiencia, columns=["Juego", "Jugador con mas experiencia"])
    df_genero_ganador = pd.DataFrame(datos_genero_ganador, columns=["Juego", "Genero ganador"])

    contador_equipos = Counter(equipo_ganadores)
    equipo_mas_ganador = contador_equipos.most_common(1)[0][0]
    #Equipo mas ganador de toda la simulacion.

    contador_generos = Counter()
    for resultados in victorias_por_generos:
        for genero, victorias in resultados.items():
            contador_generos[genero] += victorias

    # Obtener el género más ganador
    genero_mas_ganador = contador_generos.most_common(1)[0][0]
    
    return df_equipo_ganador, df_equipo_perdedor, df_jugador_suerte, df_jugador_experiencia, df_genero_ganador, equipo_mas_ganador, genero_mas_ganador

        
   

if __name__ == '__main__':
    simular_juegos(20000)

