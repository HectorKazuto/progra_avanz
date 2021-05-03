clientes = int(input("Cuantos clientes hay?"))

Costo = float(input("Cual es el monto a pagar? "))
Pago = float(input("Cual es el monto recivido? "))



def caja_registradora (Pago, Costo):
	cambio = float(Pago - Costo)
	if cambio > 0:
		print("El cambio es: ", cambio)
		print("Paga con:")
	else:
		print("Eh compa, falta feria, dame", -(cambio), "pesos")

	i = float(0)
	while i < (cambio-500):
		billete500 += 1
		i += 500
	while i <= (cambio-200):
		billete200 += 1
		i += 200
	while i <= (cambio-100):
		billete100 += 1
		i += 100
	while i <= (cambio - 50):
		billete50 += 1
		i += 50
	while i <= (cambio - 20):
		billete20 += 1
		i += 20
	while i <= (cambio - 10):
		moneda10 += 1
		i += 10
	while i <= (cambio - 5):
		moneda5 += 1
		i += 5
	while i <= (cambio - 2):
		moneda2 += 1
		i += 2
	while i <= (cambio - 1):
		moneda1 += 1
		i += 1
	while i <= (cambio - 0.50):
		moneda50c += 1
		i += 0.50

	if billete500 > 0:
		print(billete500, "billetes de 500")
	if billete200 > 0:
		print(billete200, "billetes de 200")
	if billete100 > 0:
		print(billete100, "billetes de 100")
	if billete50 > 0:
		print(billete50, "billetes de 50")
	if billete20 > 0:
		print(billete20, "billetes de 20")
	if moneda10 > 0:
		print(moneda10, "monedas de 10")
	if moneda5 > 0:
		print(moneda5, "monedas de 5")
	if moneda2 > 0:
		print(moneda2, "monedas de 2")
	if moneda1 > 0:
		print(moneda1, "monedas de 1")
	if moneda50c > 0:
		print(moneda50c, "monedas de 50 centavos")

i=0
while i < clientes:
	caja_registradora(Pago, Costo)
	i += 1