
numero = int(input("Ingresa el número para generar su tabla de multiplicar: "))

print(f"\nTabla de multiplicar del {numero}:")


for i in range(1, 13):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
