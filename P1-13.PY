""" P-1.13 Desarrolle herencia jerarquica en base a una clase Poligono
que tiene metodos abstractos area() y perimetro(). Implemente la
clase Triangulo, Cuadrilatero, Pentagono, Hexagono, y Octagono que
extienda esta clase base, con los metodos area() y perimetro().
Tambien implemente la clase TriaguloIsosceles, TrianguloEquilatero,
Rectangulo y Cuadrado, que tienen las relaciones de herencia apropiadas.
Finalmente escriba un programa sencillo que permita a los usuarios crear
poligonos de varios tipos introduciendo sus dimensiones geometricas y el
programa muestre el  ́area y el perimetro. """

import math

class Poligono:
    def area(self):
        pass
    
    def perimetro(self):
        pass

class Triangulo(Poligono):
    def __init__(self, lado1, lado2, lado3):
        self.a = lado1
        self.b = lado2
        self.c = lado3
    
    def area(self):
        s = (self.a + self.b + self.c) / 2
        resul = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return resul
    
    def perimetro(self):
        return self.a + self.b + self.c
    
class Cuadrilatero(Poligono):
    def __init__(self, lado1, lado2, lado3, lado4):
        self.a = lado1
        self.b = lado2
        self.c = lado3
        self.d = lado4
    
    def area(self):
        s = (self.a + self.b + self.c + self.d) / 2
        resul = math.sqrt((s - self.a) * (s - self.b) * (s - self.c) * (s - self.d))
        return resul
    
    def perimetro(self):
        return self.a + self.b + self.c + self.d

class Pentagono(Poligono):
    def __init__(self, lado):
        self.a = lado
    
    def area(self):
        return (1.720 * self.a ** 2) / 4
    
    def perimetro(self):
        return 5 * self.a

class Hexagono(Poligono):
    def __init__(self, lado):
        self.a = lado
    
    def area(self):
        return (3 * (3 ** 0.5) * self.a ** 2) / 2
    
    def perimetro(self):
        return 6 * self.a
    
class Octagono(Poligono):
    def __init__(self, lado):
        self.a = lado
    
    def area(self):
        return 2 * (1 + (2 ** 0.5)) * self.a ** 2
    
    def perimetro(self):
        return 8 * self.a

class TrianguloIsosceles(Triangulo):
    def __init__(self, lado1, lado2, lado3):
        super().__init__(lado1, lado2, lado3)

class TrianguloEquilatero(Triangulo):
    def __init__(self, lado):
        super().__init__(lado, lado, lado)

class Rectangulo(Cuadrilatero):
    def __init__(self, lado, lado2):
        super().__init__(lado, lado2, lado, lado2)

class Cuadrado(Cuadrilatero):
    def __init__(self, lado):
        super().__init__(lado, lado, lado, lado)




#caso de prueba
def crear_poligono():
    tipo = input("Ingrese el tipo de polígono (Triangulo(1), Cuadrilatero(2), Pentagono(3), Hexagono(4), "
             "Octagono(5), TrianguloIsosceles(6), TrianguloEquilatero(7), Rectangulo(8), Cuadrado(9))\n"
             "-> 'dime el numero': ")
    
    if tipo == "1":
        a = float(input("Ingrese el lado 1 del triángulo: "))
        b = float(input("Ingrese el lado 2 del triángulo: "))
        c = float(input("Ingrese el lado 3 del triángulo: "))
        poligono = Triangulo(a, b, c)
    elif tipo == "2":
        a = float(input("Ingrese el lado 1 del cuadrilátero: "))
        b = float(input("Ingrese el lado 2 del cuadrilátero: "))
        c = float(input("Ingrese el lado 3 del cuadrilátero: "))
        d = float(input("Ingrese el lado 4 del cuadrilátero: "))
        poligono = Cuadrilatero(a, b, c, d)
    elif tipo == "3":
        lado = float(input("Ingrese el lado del pentágono: "))
        poligono = Pentagono(lado)
    elif tipo == "4":
        lado = float(input("Ingrese el lado del hexágono: "))
        poligono = Hexagono(lado)
    elif tipo == "5":
        lado = float(input("Ingrese el lado del octágono: "))
        poligono = Octagono(lado)
    elif tipo == "6":
        a = float(input("Ingrese el lado que son iguales del triángulo: "))
        b = float(input("Ingrese el lado diferente del triángulo: "))
        poligono = TrianguloIsosceles(a, a, b)
    elif tipo == "7":
        a = float(input("Ingrese el lado del triángulo: "))
        poligono = TrianguloEquilatero(a)
    elif tipo == "8":
        base = float(input("Ingrese el lado base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        poligono = Rectangulo(base, altura)
    elif tipo == "9":
        lado = float(input("Ingrese el lado del cuadrado: "))
        poligono = Cuadrado(lado)
    else:
        print("Tipo de polígono no válido.")
        return
    
    print("Área:", poligono.area())
    print("Perímetro:", poligono.perimetro())

crear_poligono()