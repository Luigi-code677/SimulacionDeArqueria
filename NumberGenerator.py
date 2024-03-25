from scipy.stats import norm


def generar_n_numeros(cantidad, generador):
    ri_values = [generador.generate_number() for _ in range(cantidad)]
    semilla = generador.semilla + 5
    return ri_values


def generar_numero_uniforme(min_value, max_value, generador_uniforme):
    return min_value + (max_value - min_value) * generador_uniforme.generate_number()


def generar_numero_normal(media, desv_estandar, generador_normal):
    return norm.ppf(generador_normal.generate_number(), media, desv_estandar)


class CongruencialLineal:
    def __init__(self, semilla):
        self.semilla = semilla
        self.k = 4779473189
        self.c = 17
        self.g = 25
        self.xn = semilla
        self.a = 1 + 2 * self.k
        self.m = 2 ** self.g

    def generate_xn(self):
        self.xn = (self.a * self.xn + self.c) % self.m
        return self.xn

    def generate_number(self):
        return self.generate_xn() / (self.m - 1)
