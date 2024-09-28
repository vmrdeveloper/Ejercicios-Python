#Calculamos descuento
def calcularDescuento(precio, descuento):
    resultado = (precio*descuento)/100
    return resultado

#Solicitamos el precio
precio = float(input("Ingrese el precio: "))
descuento = float(input("Ingrese el descuento: "))
precioFinal = precio-calcularDescuento(precio,descuento)

#Mostrando resultados
print(f"El precio del articulo es: {precio}")
print(f"El {descuento} % de descuento es: {calcularDescuento(precio,descuento)} ")
print(f"El precio final es: {precioFinal}")