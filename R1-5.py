""" R-1.5 Modifique el metodo __sub__ para la clase Vector, de forma que la
expresion u-v devuelva una instancia de vector representando la diferencia
entre dos vectores. """


class Vector:
    
    def __init__(self, d):
        self._coordenadas = [0] * d
        
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
            
    def __eq__(self, otro):
        return self._coordenadas == otro._coordenadas
    
    def __ne__(self, otro):
        return not self == otro
    
    def __str__(self):
        return '<' + str(self._coordenadas)[1:-1] + '>'



#caso de prueba 
an=Vector(3)
ar=Vector(3)

an[0]=1
an[1]=2
an[2]=3

ar[0]=3
ar[1]=2
ar[2]=1

ana=an-ar
print(ana)

