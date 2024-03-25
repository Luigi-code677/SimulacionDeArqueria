class Ronda:

    def __init__(self, numero_ronda):
        self.numero_ronda = numero_ronda
        self.lanzamientos = []

    def simularRonda(jugador):
        resistencia_actual = jugador.resistencia
        while jugador.resistencia >= 5:
            jugador.puntaje_ronda += simular_puntaje(jugador.genero)
            resistencia_actual -= 5
        recuperar_puntos(resistencia_actual, jugador)

    def simular_puntaje(genero):
        numero = generar_n_numeros(1)
        puntaje = 0
        if genero == "Hombre":
            if numero[0] <= 0.07:
                puntaje = 0
            elif 0.07 < numero[0] <= 0.47:
                puntaje = 8
            elif 0.47 < numero[0] <= 0.80:
                puntaje = 9
            else:
                puntaje = 10
        else:
            if numero[0] <= 0.05:
                puntaje = 0
            elif 0.05 < numero[0] <= 0.32:
                puntaje = 8
            elif 0.32 < numero[0] <= 0.70:
                puntaje = 9
            else:
                puntaje = 10
        return puntaje
        
    def recuperar_puntos(resistencia_anterior, jugador):
        numero = int(generar_numero_uniforme(1,2))
        jugador.resistencia = resistencia_anterior - numero