''' Crie um tipo abstrato de dado (TAD) para manipular números complexos na linguagem Python. O método deve:

- calcular três números complexos;
- realizar todas as operações básicas;
- e imprimir as propriedades real e img do números.

'''


class Complexo:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, outro_complexo):
        real = self.real + outro_complexo.real
        imag = self.imag + outro_complexo.imag
        return Complexo(real, imag)

    def __sub__(self, outro_complexo):
        real = self.real - outro_complexo.real
        imag = self.imag - outro_complexo.imag
        return Complexo(real, imag)

    def __mul__(self, outro_complexo):
        real = self.real * outro_complexo.real - self.imag * outro_complexo.imag
        imag = self.real * outro_complexo.imag + self.imag * outro_complexo.real
        return Complexo(real, imag)

    def __str__(self):
        return f'{self.real} + {self.imag}j'


# Criar três números complexos
c1 = Complexo(1, 2)
c2 = Complexo(3, 4)
c3 = Complexo(5, 6)

# Realizar operações básicas
c4 = c1 + c2
c5 = c1 - c2
c6 = c1 * c2

# Imprimir propriedades reais e imaginárias
print(f'c1: {c1.real} + {c1.imag}j')
print(f'c2: {c2.real} + {c2.imag}j')
print(f'c3: {c3.real} + {c3.imag}j')
print(f'c1 + c2: {c4}')
print(f'c1 - c2: {c5}')
print(f'c1 * c2: {c6}')
