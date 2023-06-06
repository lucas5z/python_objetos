""" C-1.10: La clase TarjetaCreditoDepredadora proporciona un m ́etodo
proceso mensual que modele el cierre de un ciclo mensual. Modifique la
clase de forma que cuando un cliente hace diez llamadas al metodo cargar
en el mes actual, cada llamada adicional a la funcion resulte en un cargo
de $1. """


from Tarjeta_import import TarjetaCredito

class TarjetaCreditoDepredadora(TarjetaCredito):

    
    def __init__(self, cliente, banco, cuenta, limite, interes, balance=0):
        
        
        super().__init__(cliente, banco, cuenta, limite,balance)
        self._interes = interes
        self._cargo_llamadas=0

    def cargar(self, precio):
        
        

        exito = super().cargar(precio)
        if not exito:
            self._balance += 5
        
        self._cargo_llamadas +=1
        if self._cargo_llamadas>10:
            self._balance+=1
         
        return exito
    
    def proceso_mensual(self):
    
        if self._balance > 0:
            factor_mensual = pow(1 + self._interes, 1/12)
            self._balance *= factor_mensual
        self._cargo_llamadas=0



#caso de prueba

tarjeta_arm = TarjetaCreditoDepredadora("Juan", "BCP", "132312", 1300, 0.08)


tarjeta_arm.cargar(100)
tarjeta_arm.cargar(100)
tarjeta_arm.cargar(100)
tarjeta_arm.cargar(100)
tarjeta_arm.cargar(100)
tarjeta_arm.cargar(100)
tarjeta_arm.cargar(100)
tarjeta_arm.cargar(100)
tarjeta_arm.cargar(100)
tarjeta_arm.cargar(100)
tarjeta_arm.cargar(100)
tarjeta_arm.cargar(100)


print("Balance:", tarjeta_arm.get_balance())  
print("Cargas realizadas:", tarjeta_arm._cargo_llamadas) 

tarjeta_arm.proceso_mensual()

print("Balance después del proceso mensual:", tarjeta_arm.get_balance()) 
print("Cargas realizadas después del proceso mensual:", tarjeta_arm._cargo_llamadas) 

