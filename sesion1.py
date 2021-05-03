a = 12
b = 5.5

if a < b: # Verificar si a es menos que b
	print("a es menor que b")
elif a > b:  # Verificar si b es menor que a
	print("b es menor que a")
else: #imprimir si son iguales
	print("a es igual a b")

###################################

# USAR ARREGLOS > ARRAYAS
# [dato1, dato2, dato3, dato4]
# LIST -> ["hola", "mundo", 2, 3.5]...PUEDEN SER DIFS
# INDEXAR -> 0: "hola", 1: "mundo",...-1

nombres = ["hector", "manuel", "arturo", "alvaro"]

cuantos = len(nombres)
# USAR UN CICLO
# WHILE, FOR, DO WHILE
# FOR

for i in nombres:
	print(i)
print("---------------------")
for i in range(cuantos):
	print(nombres[i])

abc = "abcdefghijklmnopqrstuvwxyz"

for letra in abc:
	if letra == "i":
		break
	print(letra+")")

while i < cuantos:
	print("aaaaaaaaah")
	i+=1 # i = i + 1

# DATOS DE USUARIO > TEMRINAL
# INPUT() : STRING
# PARSE O CAST -> INT, FLOAT, STRING...
nombre = input("Ingresa tu nombre:")
print("Tu nombre es: " + nombre)

edad = int(input("ingresa tu edad:"))
print("Tu edad es: " + edad)

if edad < 18:
	print("No puedes tomas!")
else:
	print("TOMAR")


### EJERCICIO

# Pedir n (el usuario lo da) nombres al usuario, lo van a guardar en una lista (list)
# Print al revés a la lista
# Enviar por correo: alvaro.moreno@cetys.mx