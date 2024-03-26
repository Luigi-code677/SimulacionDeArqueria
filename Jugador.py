from Lanzamiento import Lanzamiento

#Se usa montecarlo para simular el puntaje de los lanzamientos, teniendo en cuenta la tabla otorgada en el enunciado.
def simular_puntaje(genero, generador):
    numero = generador.generate_number()
    puntaje = 0
    if genero == "Hombre":
        if numero <= 0.07:
            puntaje = 0
        elif 0.07 < numero <= 0.47:
            puntaje = 8
        elif 0.47 < numero <= 0.80:
            puntaje = 9
        else:
            puntaje = 10
    else:
        if numero <= 0.05:
            puntaje = 0
        elif 0.05 < numero <= 0.32:
            puntaje = 8
        elif 0.32 < numero <= 0.70:
            puntaje = 9
        else:
            puntaje = 10
    return puntaje

#Se simula un lanzamiento.
def realizar_lanzamiento(tipo, puntaje, lanzamientos):
    lanzamiento = Lanzamiento(tipo, puntaje)
    lanzamientos.append(lanzamiento)

#Se inicializa la clase Jugador.
class Jugador:
    def __init__(self, nombre, genero, suerte, resistencia, experiencia, generador):
        self.nombre = nombre
        self.genero = genero
        self.suerte = suerte
        self.resistencia = resistencia
        self.resistencia_total = resistencia
        self.experiencia_inicial = experiencia
        self.experiencia = experiencia
        self.rondas = []
        self.rondas_extra = []
        self.contador_suerte = 0
        self.contador_experiencia_resistencia = 0
        self.generador = generador

    #Calcula el puntaje obtenido en una ronda específica.
    def obtener_puntaje_ronda_equipo(self, numero_ronda):
        ronda = self.rondas[numero_ronda]
        puntaje = 0
        for lanzamiento in ronda:
            puntaje += lanzamiento.puntaje if lanzamiento.tipo == "Normal" or lanzamiento.tipo == "Equipo" else 0
        return puntaje

    #Calcula el puntaje obtenido por un jugador en una ronda específica.
    def obtener_puntaje_ronda_individual(self, numero_ronda):
        ronda = self.rondas[numero_ronda]
        puntaje = 0
        for lanzamiento in ronda:
            puntaje += lanzamiento.puntaje if lanzamiento.tipo == "Normal" or lanzamiento.tipo == "Individual" else 0
        return puntaje
    
    #Calcula el puntaje total sumando los puntajes de todas las rondas.
    def obtener_puntaje_total_equipo(self):
        puntaje = 0
        for i in range(len(self.rondas)):
            puntaje += self.obtener_puntaje_ronda_equipo(i+1)
        return puntaje

    #Calcula el puntaje total de un jugador sumando los puntajes de todas las rondas.
    def obtener_puntaje_total_individual(self):
        puntaje = 0
        for i in range(len(self.rondas)):
            puntaje += self.obtener_puntaje_ronda_individual(i)
        return puntaje
    
    #Simula una ronda de juego para el jugador o equipo y registra los lanzamientos realizados.
    def simular_ronda(self) -> int:
        resistencia_actual = self.resistencia
        lanzamientos = []
        while self.resistencia >= 5:
            realizar_lanzamiento("Normal", simular_puntaje(self.genero, self.generador), lanzamientos)
            if self.experiencia >= self.experiencia_inicial + 9 and self.contador_experiencia_resistencia < 2:
                self.resistencia -= 1
                self.contador_experiencia_resistencia += 1
            else:
                self.resistencia -= 5
        self.recuperar_puntos(resistencia_actual)
        self.rondas.append(lanzamientos)
        return len(self.rondas)-1
    
    #Realiza un lanzamiento extra para el equipo en una ronda específica.
    def lanzamiento_extra_equipo(self, ronda):
        realizar_lanzamiento("Equipo", simular_puntaje(self.genero, self.generador), self.rondas[ronda])
        self.contador_suerte += 1

    #Realiza un lanzamiento extra para un jugador en una ronda específica.
    def lanzamiento_extra_individual(self, ronda):
        realizar_lanzamiento("Individual", simular_puntaje(self.genero, self.generador), self.rondas[ronda])

    # Recupera los puntos de resistencia del jugador o equipo.
    def recuperar_puntos(self, resistencia_anterior):
        numero = self.generador.generate_number()
        puntos = 2 if numero <= 0.5 else 1
        self.resistencia = resistencia_anterior - puntos
