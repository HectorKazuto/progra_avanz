#Modulo calculadora

#Sumar
def sumar(num1, num2):
	return (num1 + num2)

#Restar
def restar(num1, num2):
	return (num1 - num2)

#Multiplicar
def multiplicar(num1, num2):
	return (num1 * num2)

#Dividir
def dividir(num1, num2):
	return (num1 / num2)

#Exponente 
def elevar (base, exp):
	temp = base
	for x in range(exp-1):
		temp *= base
	return temp


print(str(sumar(1,2)))
print(str(restar(5,3)))
print(str(multiplicar(5,6)))
print(str(dividir(25,5)))
print(str(elevar(2,3)))