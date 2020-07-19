'''Exercício 1: Uma classe para triângulos
Defina a classe Triangulo cujo construtor recebe 3 valores inteiros
correspondentes aos lados a, b e c de um triângulo.

A classe triângulo também deve possuir um método perimetro, que não
recebe parâmetros e devolve um valor inteiro correspondente ao perímetro do triângulo.'''

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
      perimetro = self.a + self.b + self.c
      return perimetro
    
    def tipo_lado(self):
      if self.a == self.b and self.b == self.c:
        return 'equilátero'
      elif self.a != self.b and self.a != self.c and self.b != self.c:
        return 'escaleno'
      else:
        return 'isósceles'

    def retangulo(self):
        if self.a**2 == self.b**2 + self.c**2:
            return True
        elif self.b**2 == self.a**2 + self.c**2:
            return True
        elif self.c**2 == self.a**2 + self.b**2:
            return True
        else:
            return False

    def sorted_lista(self):
        lista = [self.a, self.b, self.c]
        return sorted(lista)

    def semelhantes(self, t2):
        t1 = self.sorted_lista()
        t2 = t2.sorted_lista()
        i = 0
        semelhantes = True
        while i < len(t1):
            for lado in t2:
                if lado % t1[i] != 0:
                  semelhantes = False
            i += 1
        return semelhantes

            
        
    
