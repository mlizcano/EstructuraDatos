import os
os.system('cls' if os.name == 'nt' else 'clear')
#Una cola doblemente circular requiere nodos que
#tengan referencias tanto al siguiente como al
#anterior nodo. En este caso, también se utiliza
#un nodo centinela para simplificar las operaciones
#de inserción y eliminación.

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ColaDoblementeCircular:
    def __init__(self):
        self.nodo_centinela = Nodo(None)  # Nodo centinela
        self.nodo_centinela.siguiente = self.nodo_centinela
        self.nodo_centinela.anterior = self.nodo_centinela

    def encolar(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.anterior = self.nodo_centinela.anterior
        nuevo_nodo.siguiente = self.nodo_centinela
        self.nodo_centinela.anterior.siguiente = nuevo_nodo
        self.nodo_centinela.anterior = nuevo_nodo

    def desencolar(self):
        if self.nodo_centinela.siguiente == self.nodo_centinela:
            print("La cola está vacía")
            return
        nodo_a_eliminar = self.nodo_centinela.siguiente
        nodo_a_eliminar.siguiente.anterior = self.nodo_centinela
        self.nodo_centinela.siguiente = nodo_a_eliminar.siguiente
        return nodo_a_eliminar.valor

    def mostrar(self):
        actual = self.nodo_centinela.siguiente
        while actual != self.nodo_centinela:
            print(actual.valor, end=" ")
            actual = actual.siguiente
        print()

# Uso de la cola doblemente circular
cola_doblemente_circular = ColaDoblementeCircular()
cola_doblemente_circular.encolar(1)
cola_doblemente_circular.encolar(2)
cola_doblemente_circular.encolar(3)
cola_doblemente_circular.mostrar()
cola_doblemente_circular.desencolar()
cola_doblemente_circular.mostrar()
