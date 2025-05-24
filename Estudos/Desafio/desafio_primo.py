from numpy import random

numero_aleatorio= random.randint(100)

def jogo():
    while True:
      
        palpite= int(input("Insira um número:   "))
        if palpite < numero_aleatorio:
            print("Insira um numero maior")
            continue

        elif palpite > numero_aleatorio:
            print("Insira um número menor")    
            continue

        elif palpite == numero_aleatorio:
            print(f"Parabéns o número era {numero_aleatorio}")
            break
        
        else:
            print("Digite um numero válido!")
            continue

print("Tente adivinhar o número de 1 a 100")
jogo()