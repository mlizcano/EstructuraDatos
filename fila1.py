import os
os.system('cls' if os.name == 'nt' else 'clear')
#En el uso cotidiano, una fila se refiere a una
#secuencia de personas u objetos dispuestos en una línea,
#esperando su turno para ser atendidos o procesados.

#Al igual que una cola en informática, sigue el principio FIFO,
#donde la primera persona u objeto en la línea será el primero
#en ser atendido.

#Este término es menos técnico y más utilizado en contextos
#cotidianos o en la modelización de sistemas de espera en la
#teoría de colas.

# Fila en Python
fila = []

# Añadir elementos a la fila
fila.append('cliente1')
fila.append('cliente2')
fila.append('cliente3')
print("Los elementos de la fila son:", fila)

# Atender cliente (eliminar elemento de la fila)
cliente_atendido = fila.pop(0)
print("Cliente atendido fue:", cliente_atendido)
print("Fila después de atender a un cliente son:", fila)
