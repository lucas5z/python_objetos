""" R-1.1) Escriba una clase Python, Flower, que tiene tres propiedades
de tipo str, int y float, que respectivamente representa el nombre de la
flor, su cantidad de p ́etalos y su precio. La clase debe incluir un metodo
constructor que inicialice cada variable con su valor apropiado, y la clase
debe incluir metodos para establecer el valor de cada propiedad y recuperar
el valor de cada propiedad. """


class Flower:
    def __init__(self,nombre,petalos,precio):
        self.nombre=nombre
        self.petalos=petalos
        self.precio=precio

    def new_nombre(self,nombre):
        self.nombre=nombre
    
    def new_petalo(self,petalos):
        self.petalos=petalos
    
    def new_precio(self,precio):
        self.precio=precio

    def now_nombre(self):
        return self.nombre

    def now_petalo(self):
        return self.petalos
    
    def now_precio(self):
        return self.precio
    
#caso de prueba

rosa=Flower("rosa",25,10.3)

print(rosa.now_nombre())
print(rosa.now_petalo())
print(rosa.now_precio())

rosa.new_nombre("rosa negra")
rosa.new_petalo(17)
rosa.new_precio(20.5)

print(rosa.now_nombre())
print(rosa.now_petalo())
print(rosa.now_precio())

