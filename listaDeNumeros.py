numerosIntroducidos = input("Ingresa una lista de números separados por espacios: ")

listaNumeros = [int(numero) for numero in numerosIntroducidos.split()]

listaNumeros.sort()

print("Lista ordenada de menor a mayor:", listaNumeros)

