""" R-1.9 La clase Vector proporciona un constructor que toma un entero
d, y produce un vector d-dimensional con todas las coordenadas iguales a 0.
Otra forma conveniente de crear un nuevo vector seria enviar al constructor
un parametro que es un iterable que represente una secuencia de numeros,
y se cree un vector con iguales dimensiones a la longitud de la secuencia y
coordenadas iguales a os valores de la secuencia. Por ejemplo, Vector([4,
5, 7]) produciria un vector tridimensional con coordenadas <4, 5, 7>.
Modifique el constructor de la clase Vector, de forma que ambas formas
sean aceptables, es decir que si se le envia un n ́umero  ́unico produzca un
vector de esta dimensi ́on con ceros en las coordenadas, pero si se le envia
una secuencia de numeros, produzca un vector con las coordenadas en base
a la secuencia. """

class Vector:
    
    def __init__(self, d):
        if isinstance(d, int):
            self._coordenadas = [0] * d
        elif isinstance(d, list):
            self._coordenadas = list(d)
        else:
            raise ValueError('Debe ser un entero o una secuencia de números')
        
    def __len__(self):
        return len(self._coordenadas)
    
    def __getitem__(self, j):
        return self._coordenadas[j]
    
    def __setitem__(self, j, val):
        self._coordenadas[j] = val
        
    def __add__(self, otro):
        if len(self) != len(otro):
            raise ValueError('Dimensiones deben coincidir')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + otro[j]
        return result
    def __sub__(self,otro):

        if len(self) != len(otro):
            raise ValueError("las dimensiones deben coincidir")
        
        result=Vector(len(self))
        for i in range(len(self)):
            result[i]=self[i] - otro[i]
        
        return result
    def __neg__(self):
        negativo=Vector(len(self))
        for i in range(len(self)):
            negativo[i]=self[i]*-1
        return negativo
    """  def __mul__(self,otro):
        mult=Vector(len(self))
        for i in range(len(self)):
            mult[i]=self[i]*otro
        return mult """
    def __mul__(self,otro):
        if len(self) != len(otro):
            raise ValueError("las dimensiones deben coincidir")
        mult=0
        for i in range(len(self)):
            mult+=self[i]*otro[i]
        
        return mult


    def __eq__(self, otro):
        return self._coordenadas == otro._coordenadas
    
    def __ne__(self, otro):
        return not self == otro
    
    def __str__(self):
        return '<' + str(self._coordenadas)[1:-1] + '>'


#caso de prueba 
an=Vector(3)
print(an)

ar=Vector([7,2,1])
print(ar)