import os
os.system('cls' if os.name == 'nt' else 'clear')
#En Python, una lista es una colección ordenada y mutable de elementos.
#Los elementos pueden ser de cualquier tipo y se pueden cambiar,
#agregar o eliminar.

#Las listas son estructuras de datos versátiles y
#se utilizan para almacenar una colección de objetos en un único lugar.

#Puedes acceder a los elementos por su índice, y
#las listas admiten operaciones como añadir elementos,
#eliminar elementos, iterar sobre ellos, etc.

#No siguen el principio FIFO; puedes insertar o
#eliminar elementos en cualquier posición.

# Lista en Python
lista = [1, 2, 3, 4, 5]
print("Lista original:", lista)

# Añadir elemento
lista.append(6)
print("Lista después de añadir un elemento:", lista)

# Eliminar elemento
lista.remove(3)
print("Lista después de eliminar un elemento:", lista)

# Acceder a un elemento
print("Elemento en el índice 2:", lista[2])
