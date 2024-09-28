
#Mis funciones

def suma(num1, num2):
    return num1+num2

def resta(num1, num2):
    return num1-num2

def division(num1, num2):
    return num1/num2

def multiplicacion(num1, num2):
    return num1*num2

#menu de opciones
print("Selecciona la opcion correcta: ")
print("Sumar, opcion 1.")
print("Restar, opcion 2.")
print("Dividir, opcion 3.")
print("Multiplicar, opcion 4.")


opcion=input("Ingresa la opcion deseada (1, 2, 3, 4): ")

if opcion in ['1','2','3','4']:
    num1=float(input("Ingresa el primer numero: "))
    num2=float(input("Ingrese el segundo numero: "))

    if opcion == '1':
        print(f"Resultado: {num1} + {num2} = {suma(num1, num2)}")

    elif opcion == '2':
        print(f"Resultado: {num1} + {num2} = {resta(num1,num2)}")
    
    elif opcion == '3':
        print(f"Resultado: {num1} + {num2} = {division(num1,num2)}")

    elif opcion == '4':
        print(f"Resultado: {num1} + {num2} = {multiplicacion(num1,num2)}")

else:
    print("Opcion no valida, ingresa un numero entre 1-4.") 