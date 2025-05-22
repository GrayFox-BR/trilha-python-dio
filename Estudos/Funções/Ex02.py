# 2. Crie uma função usar_pocao(hp) que aumenta o HP em 50 e retorna o novo valor.

hp = 50

def usar_pocao_hp(hp):
    return hp + 50

print (f"Usando Poção de Vida:     {hp}/100")
hp_print=usar_pocao_hp(hp)
hp=hp_print
print (f"Vida do jogador ❤️  {hp_print}/100")