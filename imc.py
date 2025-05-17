import sys


print("Hola, Este programa está diseñado para calcular el IMC, debes entregar algunos datos:")

adentro=True
while adentro:
    invalido=True
    while invalido:
        try:
            if len(sys.argv) > 1:
                masa=float(sys.argv[1])
                altura=float(sys.argv[2])
                print(f"Los datos ingresados son masa: {masa:.1f} Kg y altura: {altura:.1f} cm")
            else:
                altura=float(input("\nAltura en cm de la persona: "))
                masa=float(input("Masa de la persona en Kg: "))
            imc=masa/((altura/100)**2)
            invalido=False
        except ZeroDivisionError:
            invalido=True
            sys.argv=[]
            print("\n\nValor de altura debe ser difente a 0\n\n")
        except ValueError:
            invalido=True
            sys.argv=[]
            print("\n\nDebe ingresar valores numéricos\n\n")
        except:
            invalido=True
            sys.argv=[]
            continue;

    if 0!=imc<18.5:
        estado="con bajo peso"
    elif 18.5<=imc<25:
        estado="sana"
    elif 25<=imc<30:
        estado="con sobrepeso"
    elif 30<=imc<35:
        estado="con obesidad grado I"
    elif 35<=imc<40:
        estado="con obesidad grado II"
    else:
        estado="con obesidad grado III"
    
    print(f"\nEl IMC es {imc:.2f} \nSegun la OMS esta persona está {estado} ")
        
    pregunta=True
    while pregunta:    
        valor=input("\n¿Quieres volver a calcular el IMC? (Si/No): ")
        if (valor.lower()=="si" or valor.lower()=="s"):
            pregunta=False
        elif (valor.lower()=="no" or valor.lower()=="n"):
            pregunta=False
            adentro=False
            print("\nNos vemos en una proxima ocasión")
        else:
            print("\nValor no válido")
    