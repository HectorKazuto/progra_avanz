lista = []

n = int(input("Cuantos nombres hay en la lista? "))

print("Dime los nombres")

i = 0
while i < n:
	nombres = input("")
	lista.append(nombres)
	i = i + 1

print("-------------------")

lista.reverse()

for j in range(n):
	print(lista[j])