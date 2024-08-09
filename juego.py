from random import randint

opciones = ["piedra", "papel", "tijera"]

while True:
    valor_aleatorio = randint(0, 2)
    juego_computador = opciones[valor_aleatorio]

    juego_usuario = input("¿Qué eliges? piedra, papel, tijera: ").lower()

    if juego_usuario == juego_computador:
        print("¡Es un empate!")
    elif juego_usuario == "piedra":
        if juego_computador == "papel":
            print("¡Perdiste!", juego_computador, "cubre", juego_usuario)
        else:
            print("¡Ganaste!", juego_usuario, "aplasta", juego_computador)
    elif juego_usuario == "papel":
        if juego_computador == "tijera":
            print("¡Perdiste!", juego_computador, "corta", juego_usuario)
        else:
            print("¡Ganaste!", juego_usuario, "cubre", juego_computador)
    elif juego_usuario == "tijera":
        if juego_computador == "piedra":
            print("¡Perdiste!", juego_computador, "aplasta", juego_usuario)
        else:
            print("¡Ganaste!", juego_usuario, "corta", juego_computador)
    else:
        print("palabra no valida")
