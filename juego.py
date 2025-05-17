import sys 
import random


print("Hola, Este programa está diseñado para jugar al cachipun contra el computador\n")

adentro=True
while adentro:
    invalido=True
    while invalido:

        if len(sys.argv) > 1:
            mano=sys.argv[1]
            print(f"Lanzaste {mano}")
        else:
            mano=input("\nElige entre Piedra, Papel o Tijera: ")
        
        if mano.lower()=="tijera" or mano.lower()=="papel" or mano.lower()=="piedra":
            invalido=False
        else:
            invalido=True
            print("\n\nDebes escribir una de las 3 opciones")
            sys.argv=[]

    
    opciones=["piedra","papel","tijera"]
    compu=random.choice(opciones)
    print(f"El Computador lanzó {compu}")

    if mano.lower()==compu:
        print("\nUff Casí, Empate")
    elif mano.lower()=="piedra" and compu=="tijera":
        print("\nBien jugado, Ganaste")
    elif mano.lower()=="papel" and compu=="piedra":
        print("\nBien jugado, Ganaste")
    elif mano.lower()=="tijera" and compu=="papel":
        print("\nBien jugado, Ganaste")
    else:
        print("\nPerdiste, Sé que puedes hacerlo mejor")
    
        
    pregunta=True
    while pregunta:    
        valor=input("\n¿Quieres volver a jugar? (Si/No): ")
        if (valor.lower()=="si" or valor.lower()=="s"):
            pregunta=False
        elif (valor.lower()=="no" or valor.lower()=="n"):
            pregunta=False
            adentro=False
            print("\nNos vemos en una proxima ocasión")
        else:
            print("\nValor no válido")
    