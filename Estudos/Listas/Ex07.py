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
