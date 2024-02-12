import os
os.system('cls' if os.name == 'nt' else 'clear')
#En informática, una cola es una estructura de datos abstracta
#donde los elementos se mantienen en orden.

#Funciona bajo el principio de "Primero en Entrar,
#Primero en Salir" (FIFO, por sus siglas en inglés).
#Esto significa que el primer elemento agregado a la cola
#será el primero en ser eliminado.

#Se utiliza en situaciones donde es importante mantener
#el orden de los elementos, como en la gestión de procesos
#en sistemas operativos, operaciones de impresión, etc.

#Las operaciones típicas incluyen encolar
#(añadir un elemento al final de la cola)
#y desencolar (eliminar el elemento al frente de la cola).

class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, item):
        self.elementos.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        else:
            raise IndexError("Desencolar de una cola vacía")

    def esta_vacia(self):
        return len(self.elementos) == 0

# Uso de la Cola
cola = Cola()
cola.encolar('elemento1')
cola.encolar('elemento2')
cola.encolar('elemento3')
print("Elemento desencolado:", cola.desencolar())
