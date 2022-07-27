"""
Escribir un programa para el manejo de listas el cuál cumplirá los siguientes
requerimientos (4 ptos):
Reglas:
- Crear una función que le permitirá almacenar 10 número aleatorios e
  imprimirlos por consola.
- Crear una función que le permita almacenar los números no repetidos de la
  lista anterior, retornar este valor e imprimirlo por consola.
- Crear una función donde se creará lista para ordenar de mayor a menor la
  lista que se creará en el ítem anterior (número no repetidos) y otra lista
  para ordenarlas de menor a mayor, retornar este valor e imprimirlo por
  consola.
- Crear una función para indicar cuál es mayor número de la lista (lista del
  ítem 2), retornar este valor e imprimirlo por consola.
"""

import random

def almacenaAleatorio ():
    lista = []
    for i in range(10):
        num = random.randint(1, 50)
        lista.append(num)
    return lista

def almacenaDifAleatorio (lista):
    for i in range (10):
        if lista[i] == lista[i+1]:
            lista.remove(i)
        return lista

def ordenarMeMaAleatorio (lista):
    ordenMenorMayor = lista.sort()

def ordenarMaMeAleatorio (lista):
    ordenMayorMenor = lista.reverse()

def mayorNumero (lista):
    return max(lista)

numeros = almacenaAleatorio()
print("Numeros aleatorios generados:       {}".format(numeros))
print("Numeros aleatorios no repetidos:    {}".format(almacenaDifAleatorio(numeros)))
ordenarMeMaAleatorio(numeros)
print("Numeros ordenados de menor a mayor: {}".format(numeros))
ordenarMaMeAleatorio(numeros)
print("Numeros ordenados de mayor a menor: {}".format(numeros))

print("Mayor numero de la lista:           {}".format(mayorNumero(numeros)))