
#Recibimos el texto
texto=input("Escriba el texto: ")

#Usamos la funcion split para dividir las palabras en una lista.
palabras=texto.split()

#Con len obtenemos el numero de palabras
cantidadPalabras = len(palabras)

print(f"El texto introducido tiene {cantidadPalabras} palabras.")