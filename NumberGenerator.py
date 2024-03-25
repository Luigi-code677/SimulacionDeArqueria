class CongruencialLineal:
    def _init_(self, a, c, m, seed):
        self.a = a
        self.c = c
        self.m = m
        self.xn = seed

    def generate_xn(self):
        self.xn = (self.a * self.xn + self.c) % self.m
        return self.xn

    def generate_number(self):
        return self.generate_xn()/(self.m-1)
    