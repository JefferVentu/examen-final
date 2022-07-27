from Ejercicio02Funciones import ingresoDatos

file = open("ficheros/notas.txt", "w")

n = ingresoDatos()
a = ' '
for i in n:
    a += ' ' + i

file.write(n)