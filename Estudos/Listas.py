#1. Crie uma lista com 3 nomes e imprima cada um em uma linha

#nomes = ["Luis", "Renato","Fernandes"]
#for nome in nomes:
#    print(nome)

#Correto
#---------------------------------------------------------------

#2. Some todos os números de uma lista

# numeros = [5, 10, 15, 20]
# soma_total = 0
# for soma in numeros:
#     soma_total += soma
#     print (soma_total)

#Correto
#---------------------------------------------------------------

#3. Multiplique todos os números de uma lista por 2 e imprima os novos valores
# numeros = [1, 2, 3, 4]
# multi = 0

# for numero in numeros:
#     multi = numero * 2
#     print(multi) 
# Dica: use for e print o número vezes 2

#Correto

#---------------------------------------------------------------

#4. Verifique se um nome está dentro da lista

# nomes = ["ana", "joão", "carla"]
# nome_procurado = input("Digite um nome: ")

# if nome_procurado in nomes:
#     print(f"{nome_procurado}, este nome está na lista!")
# else:
#     print(f"{nome_procurado}, não está na lista!")

# Correto    

#---------------------------------------------------------------

# 5. Adicione 3 números digitados pelo usuário em uma lista e depois imprima a lista
# # Dica: use input() dentro de um laço e .append() na lista

# lista = []

# for i in range(3):
#      numero = int (input("Digite um numero: "))
#      lista.append(numero)

# print(lista)     

# Correto
#---------------------------------------------------------------





#lista.append - Adiciona itens a uma lista

# LISTA(NOME DA VAR LISTA) .append (Comando para adicionar), (NOME DA VARIAVEL OU ENTRADA DE DADOS)

#-----------------------------------------------------------------
#Exercício 1 – Criando o inventário
#Crie uma lista chamada inventario e adicione 3 itens iniciais que seu personagem carrega. Em seguida, imprima todos os itens com uma mensagem:

# Você possui os seguintes itens:
# Espada
# Poção de vida
# Mapa antigo

# inventario = []
# inventario.append("Espada")
# inventario.append("Poção de vida")
# inventario.append("Mapa antigo")

# for item in inventario:
#     print(item)
    
#-----------------------------------------------------------------

# Exercício 2 – Usando poções
# Você tem uma lista com 5 poções no inventário. Remova uma delas usando .remove() ou .pop() e mostre o inventário atualizado.

# inventario = ["Poção de Vida", "Poção de Mana", "Poção de Meleca", "Poção Podre", "Poção de Agilidade"]
# print(inventario)
# print("Revomendo poções estragadas ou sem serventia")

# del inventario[3]
# del inventario[2]
# print(inventario)

#Sistema de Batalha simples para fixar os conceitos de Python

inventario_jogador = ["Poção de Vida", "Poção de Mana"]
hp = 500
mana = 250
espada_ferro = 15  # dano
esqueleto_hp = 300

print("👤 Você encontrou um Esqueleto!")
print("⚔️ Batalha Iniciada!")

while hp>0 and esqueleto_hp > 0:
    print("\n Oque você quer fazer?\n")
    print("1. Atacar com Espada.")
    print("2. Usar poção de vida")
    print("3. Usar poção de mana")
    print("4. Usa Mágia - Luz Divina")
    luz_divina_cost=50
    luz_divina_damage=30
    escolha = input("Escolha uma ação (1,2,3 ou 4)\n")

    if escolha == "1":
        print("Você atacou o esqueleto, com espada de ferro\n")
        esqueleto_hp -= espada_ferro
        print(f" Vida do esqueleto: ❤️  {esqueleto_hp}/300")

    elif escolha == "2":
        if "Poção de Vida" in inventario_jogador:
            hp += 100
            inventario_jogador.remove("Poção de Vida")
            print (f" Vida do jogador: ❤️   {hp}/500")

        print("Você não tem mais poção de vida")
    
    elif escolha == "3":
        if "Poção de Mana" in inventario_jogador:
            mana += 100
            inventario_jogador.remove("Poção de Mana")
            print(f"Mana do jogador: 🪄   {mana}/300")

        print("Você não tem mais poção de mana")

    elif escolha =="4" :
        if mana >= luz_divina_cost:
            mana-=luz_divina_cost
            print("Jogador usa Luz Divina\n")   
            print(f"Mana do jogador: 🪄     {mana}/ 300")
            print("Esqueleto é atigindo por Luz Divina.\n")
            esqueleto_hp -= luz_divina_damage
            print(f"Vida do Esqueleto: ❤️   {esqueleto_hp}/300")

        print("Você não tem mana o suficiente!\n")

    else:
        
        print ("Escolha inválida")


    if esqueleto_hp > 0:
        
        print("O esqueleto ataca")
        hp -= 20 
        print (f" Vida do jogador: ❤️   {hp}/500")

if hp <= 0:
    print("\n Você foi derrotado!")
elif esqueleto_hp <=0:
    print("\n Você derrotou o Esqueleto!")
