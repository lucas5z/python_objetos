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