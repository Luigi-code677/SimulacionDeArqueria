
k = 47794729  # Valor k
c = 11  # Valor c
g = 20  # Valor g

a = 1 + 2 * k
m = 2 ** g
semilla = 42


class CongruencialLineal:
    def __init__(self, seed):
        self.xn = seed

    def generate_xn(self):
        self.xn = (self.a * self.xn + self.c) % self.m
        return self.xn

    def generate_number(self):
        return self.generate_xn()/(self.m-1)
    