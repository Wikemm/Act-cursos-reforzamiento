imc = 'calcular el IMC'
print("Calculo de IMC")

# primero solicitamos al usuario que ingrese los datos

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

# calculamos el IMC

imc = peso / (altura ** 2)

print(f"Su IMC es: {imc:.2f}\n")
