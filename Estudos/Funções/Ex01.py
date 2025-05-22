# 🧠 Bora praticar? Aqui vão 3 exercícios simples com funções:
# 1. Crie uma função mostrar_inventario() que imprime os itens de uma lista.

# 3. Crie uma função batalha(jogador_hp, inimigo_hp) que imprime quem ganhou.

#1. 
def mostrar_inventario ():
    inventario=["Poção de Vida", "Poção de Mana", "Espada de Madeira", "Moedas"]
    for i , item in enumerate(inventario, 1):

        print(f"{i}.{item}")

mostrar_inventario()
