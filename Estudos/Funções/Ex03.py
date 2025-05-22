# 3. Crie uma função batalha(jogador_hp, inimigo_hp) que imprime quem ganhou.

jogador_hp = 100
inimigo_hp = 100

def turno_jogador(inimigo_hp):
    print("Jogador ataca inimigo!")
    print(f"Vida do inimigo {inimigo_hp - 50}")
    return inimigo_hp - 50

def turno_inimigo (jogador_hp):
    print("Inimigo ataca jogador!")
    print (f"Vida do jogador {jogador_hp-50}")
    return jogador_hp - 50 

# while jogador_hp >=0 :
    
# breakpoint
# if jogador_hp <0:
#         jogador_hp=turno_jogador(jogador_hp)
    
#         inimigo_hp=turno_inimigo(inimigo_hp)  
# else:
#         print("O jogador foi derrotado!")


def batalha(jogador_hp, inimigo_hp):
    while jogador_hp > 0 and inimigo_hp > 0:
        inimigo_hp = turno_jogador(inimigo_hp)
        if inimigo_hp <= 0:
            print("🎉 O jogador venceu!")
            break

        jogador_hp = turno_inimigo(jogador_hp)
        if jogador_hp <= 0:
            print("💀 O inimigo venceu!")
            break

batalha(jogador_hp,inimigo_hp)

#o chat resolveu esse para mim, usando uma função para chamar a batalha usou operador AND dentro de while e um if para verificar a vida de cada um
#Usou o comando BREAK para interromper o while, ou seja posso deixar uma verificação rodar com o while e usar o break de interruptor.
