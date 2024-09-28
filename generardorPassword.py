import random
import string

def generar_password(longitud):
    # Definir los caracteres permitidos para la contraseña
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Generar la contraseña aleatoria combinando caracteres
    password = ''.join(random.choice(caracteres) for i in range(longitud))
    
    return password


longitud = int(input("Especifica la longitud deseada de la contraseña: "))
    
password_generado = generar_password(longitud)
print(f"El password generado es: {password_generado}")