import os
os.system('cls' if os.name == 'nt' else 'clear')
#Una cola circular puede implementarse usando una lista
#con una capacidad fija y dos índices para hacer
#un seguimiento del inicio y el final de la cola.

class ColaCircular:
    def __init__(self, capacidad):
        self.cola = [None] * capacidad
        self.capacidad = capacidad
        self.inicio = self.fin = -1

    def encolar(self, valor):
        if (self.fin + 1) % self.capacidad == self.inicio:
            print("La cola está llena")
        elif self.inicio == -1:
            self.inicio = 0
            self.fin = 0
            self.cola[self.fin] = valor
        else:
            self.fin = (self.fin + 1) % self.capacidad
            self.cola[self.fin] = valor

    def desencolar(self):
        if self.inicio == -1:
            print("La cola está vacía")
        elif self.inicio == self.fin:
            self.inicio = -1
            self.fin = -1
        else:
            self.inicio = (self.inicio + 1) % self.capacidad

    def mostrar(self):
        if self.inicio == -1:
            print("La cola está vacía")
        else:
            index = self.inicio
            while True:
                print(self.cola[index], end=" ")
                if index == self.fin:
                    break
                index = (index + 1) % self.capacidad
            print()

# Uso de la cola circular
cola_circular = ColaCircular(5)
cola_circular.encolar(1)
cola_circular.encolar(2)
cola_circular.encolar(3)
cola_circular.mostrar()
cola_circular.desencolar()
cola_circular.mostrar()
