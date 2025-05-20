#Exercício 1 – Criando o inventário
#Crie uma lista chamada inventario e adicione 3 itens iniciais que seu personagem carrega. Em seguida, imprima todos os itens com uma mensagem:

# Você possui os seguintes itens:
# Espada
# Poção de vida
# Mapa antigo

inventario = []
inventario.append("Espada")
inventario.append("Poção de vida")
inventario.append("Mapa antigo")

for item in inventario:
    print(item)
    
#-----------------------------------------------------------------

# Exercício 2 – Usando poções
# Você tem uma lista com 5 poções no inventário. Remova uma delas usando .remove() ou .pop() e mostre o inventário atualizado.

inventario = ["Poção de Vida", "Poção de Mana", "Poção de Meleca", "Poção Podre", "Poção de Agilidade"]
print(inventario)
print("Revomendo poções estragadas ou sem serventia")

del inventario[3]
del inventario[2]
print(inventario)

#Sistema de Batalha simples para fixar os conceitos de Python
