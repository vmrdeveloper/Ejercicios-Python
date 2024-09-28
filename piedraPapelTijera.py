import random

#opciones a elegir
opcion = ["piedra", "papel", "tijera"]

def play():
    print("Reglas del juego: debe seleccionar una opcion entre piedra, papel o tijera.")
    print("Si selecciona dos respuestas iguales empata, piedra mata a tijera, papel mata a piedra y tijera mata a papel.")

    jugador = input("Seleccione una opcion: ").lower()

    if jugador not in opcion:
        print("Debe seleccionar una opcion valida (piedra, papel o tijera).")
        return

    bot = random.choice(opcion)
    print(f"bot eligio: {bot}")

    if jugador == bot:
        print("¡Es un empate!")
    elif (jugador == "piedra" and bot == "tijeras") or \
         (jugador == "papel" and bot == "piedra") or \
         (jugador == "tijeras" and bot == "papel"):
        print("¡Ganaste!")
    else:
        print("Perdiste. ¡Inténtalo de nuevo!")


play()


