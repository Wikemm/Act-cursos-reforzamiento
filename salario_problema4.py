salario = 'calcular salario neto'
print("Calculo del salario neto")

# primero solicitamos al usuario que ingrese los datos

salario_bruto = float(input("Ingrese el salario bruto: $"))
porcentaje_impuesto = float(input("Ingrese el porcentaje de impuesto (a descontar): "))
deducciones = float(input("Ingrese el monto de deducciones: $"))

#calculamos el salario neto

descuento_impuesto = (salario_bruto * porcentaje_impuesto) / 100
salario_neto = salario_bruto - descuento_impuesto
print(f"El salario neto es: {salario_neto:.2f}")
