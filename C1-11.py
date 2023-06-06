""" C-1.11: Modifique la clase TarjetaCreditoDepredadora de forma que
a un cliente le es asignado un pago minimo mensual, como un porcentaje
del balance, de esta forma se le carga un impuesto por mora si el cliente
no paga el monto minimo antes del siguiente ciclo mensual. """

from Tarjeta_import import TarjetaCredito

class TarjetaCreditoDepredadora(TarjetaCredito):

    
    def __init__(self, cliente, banco, cuenta, limite, interes,pago_minimo, balance=0):
        
        
        super().__init__(cliente, banco, cuenta, limite,balance)
        self._interes = interes
        self._cargo_llamadas=0
        self._pago_minimo=pago_minimo

    def cargar(self, precio):
        
        

        exito = super().cargar(precio)
        if not exito:
            self._balance += 5
        
        self._cargo_llamadas +=1
        if self._cargo_llamadas>10:
            self._balance+=1
         
        return exito
    
    def pago_minimo(self,pago):
        super().pagar(pago)
        if self._pago_minimo == pago:
            self._pago_minimo=0

    def proceso_mensual(self):
    
        if self._balance > 0:
            factor_mensual = pow(1 + self._interes, 1/12)
            self._balance *= factor_mensual

        self._cargo_llamadas=0

        if self._balance > 0 and self._balance * self._pago_minimo != 0:
            impuesto_mora = self._balance * 0.05  # Impuesto por mora del 5% del balance
            self._balance += impuesto_mora



#caso de prueba
tarjeta_arm = TarjetaCreditoDepredadora("Juan", "BCP", "132312", 1000, 0.05, 0.10)

tarjeta_arm.cargar(500)
tarjeta_arm.cargar(200)
tarjeta_arm.cargar(300)

paga=input("pagaste el pago minimo asignado : (si) , (no) ")
if paga == "si":

    print("Balance:", tarjeta_arm.get_balance()) 
    tarjeta_arm.pago_minimo(0.10)
    tarjeta_arm.proceso_mensual()
    print("Balance después del proceso mensual:", tarjeta_arm.get_balance()) 

elif paga == "no":
    print("Balance antes del proceso mensual:", tarjeta_arm.get_balance())
    tarjeta_arm.proceso_mensual()
    print("Balance después del proceso mensual:", tarjeta_arm.get_balance()) 