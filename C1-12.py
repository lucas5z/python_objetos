""" C-1.12 Implemente un metodo set balance(b) para la clase
TarjetaCredito, de modo que pueda ser usada por las clases derivadas,
sin que esta tenga que acceder directamente al miembro de datos balance. """

class TarjetaCredito:

    def __init__(self, cliente, banco, cuenta, limite, balance=0):
        
        self._cliente = cliente
        self._banco = banco
        self._cuenta = cuenta
        self._limite = limite
        self._balance = balance

    def get_cliente(self):
       
        return self._cliente

    def get_banco(self):
       
        return self._banco

    def get_cuenta(self):
 
        return self._cuenta

    def get_limite(self):

        return self._limite

    def get_balance(self):

        return self._balance
    
    def _set_balance(self,b):
        if not isinstance(b,(int,float)):
            raise ValueError("El balance debe ser un numero")
        self._balance=b

    def cargar(self, precio):
        if not isinstance(precio, (int,float)):
            raise ValueError("El precio debe ser un número")
        
        
        if precio + self._balance > self._limite:  
            return False                           
        else:
            self._balance += precio
            return True

    def pagar(self, monto):
        if not isinstance(monto, (int, float)):
            raise TypeError("El monto debe ser un número")
        if monto < 0:
            raise ValueError("El precio es un valor negativo ")
        
        self._balance -= monto


tarjeta_arm = TarjetaCredito("Juan Perez", "BCP", "132312", 3000)

tarjeta_arm._set_balance(1500)  

print(tarjeta_arm.get_balance()) 