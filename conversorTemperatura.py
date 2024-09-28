def celsiusAFarenheit(temperatura):
    return temperatura*1.8+32

def farenheitACelcius(temperatura):
    return (temperatura-32)*0.5555

#Menu para seleccionar temperatura a convertir.

print("Que tipo de conversion que desea: ")
print("De Celsius a Farenheit: Opcion 1.")
print("De Farenheit a Celsius: Opcion 2.")

#Confirmamos la opcion

opcion = input("Digite opcion deseada: ")

if opcion in ['1', '2']:
    temperatura = float(input("Digite la temperatura: "))

    if opcion == '1':
        print(f"{temperatura} grados celsius son {celsiusAFarenheit(temperatura)} grados farenheit")

    elif opcion == '2':
        print(f"{temperatura} grados farenheit son {farenheitACelcius(temperatura)} grados celsius")

else:
    print("Seleccione una opcion correcta, debe ser 1 o 2.")



