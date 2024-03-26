from scipy.stats import norm

"Genera una lista de números pseudoaleatorios utilizando un generador congruencial lineal."
def generar_n_numeros(cantidad, generador):
    ri_values = [generador.generate_number() for _ in range(cantidad)]
    semilla = generador.semilla + 5
    return ri_values

#Genera un número pseudoaleatorio distribuido uniformemente en el intervalo [min_value, max_value].
def generar_numero_uniforme(min_value, max_value, generador_uniforme):
    return min_value + (max_value - min_value) * generador_uniforme.generate_number()

#Genera un número pseudoaleatorio con distribución normal.
def generar_numero_normal(media, desv_estandar, generador_normal):
    return norm.ppf(generador_normal.generate_number(), media, desv_estandar)

#Clase para generar números pseudoaleatorios mediante el método de Congruencial Lineal.
class CongruencialLineal:
    def __init__(self, semilla):
        self.semilla = semilla
        self.k = 477947
        self.c = 3
        self.g = 30
        self.xn = semilla
        self.a = 1 + 2 * self.k
        self.m = 2 ** self.g
    # Genera el próximo número pseudoaleatorio en la secuencia.
    def generate_xn(self):
        self.xn = (self.a * self.xn + self.c) % self.m
        return self.xn
    #Genera un número pseudoaleatorio en el rango [0, 1).
    def generate_number(self):
        return self.generate_xn() / (self.m - 1)
