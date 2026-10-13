class Vehiculo:
    def __init__(self, marca):
        self.marca = marca
        self.velocidad = 0

    def __repr__(self):
        return f"Marca: {self.marca}, Velocidad: {self.velocidad}"

    def acelerar(self):
        self.velocidad += 10

    def frenar(self):
        if self.velocidad > 0:
            self.velocidad -= 10
        else:
            self.velocidad = 0

class Carro(Vehiculo):
    def __init__(self, marca, puertas):
        super().__init__(marca)
        self.puertas = puertas

    def __repr__(self):
        return super().__repr__() + f" puertas {self.puertas}"

class Moto(Vehiculo):
    def acelerar(self):
        self.velocidad += 20

c = Carro("Mazda", 4)
print(c)

m = Moto("DT")
m.acelerar()
m.frenar()
m.frenar()
m.frenar()
print(m)