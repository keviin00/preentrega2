class Cliente:
    def __init__(self, nombre, correo, direccion, saldo):
        self.nombre = nombre
        self.correo = correo
        self.direccion = direccion
        self.saldo = saldo

    def comprar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"{self.nombre} ha realizado una compra de ${cantidad}. Saldo restante: ${self.saldo}")
        else:
            print(f"Saldo insuficiente para realizar la compra.")

    def recargar_saldo(self, cantidad):
        self.saldo += cantidad
        print(f"{self.nombre} ha recargado su saldo con ${cantidad}. Saldo actual: ${self.saldo}")

    def __str__(self):
        return f"Cliente: {self.nombre}, Correo: {self.correo}, Dirección: {self.direccion}, Saldo: ${self.saldo}"
