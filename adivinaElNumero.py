import random

#Generamos el numero aleatorio
numeroAleatorio = random.randint(1,100)

#Explicamos las reglas a seguir
print("Reglas del juego.")
print("Se proporcionara un numero aleatorio entre 1 y 100, su deber es adivinar cual es.")

numero = None

#Realizamos un bucle que se producira mientras el numero no sea adivinado
while numero != numeroAleatorio:
    numero = int(input("Ingresa el numero: "))
    if numero < numeroAleatorio:
        print("Intenta con un numero mas alto.")
    
    elif numero > numeroAleatorio:
        print("Intenta con un numero mas bajo")
    
    else:
        print("Felicidades, adivinaste el numero!!")
        

print(numeroAleatorio)
