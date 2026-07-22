promedios = 'calcular promedios'
print("Calculo de promedios")

#primero solicitamos al usuario que ingrese los datos

num1 = float(input("Ingrese la primera nota: "))
num2 = float(input("Ingrese la segunda nota: "))
num3 = float(input("Ingrese la tercera nota: "))

#calculamos el promedio

promedio = (num1 + num2 + num3) / 3
print(f"El promedio de las notas es: {promedio:.2f}")
