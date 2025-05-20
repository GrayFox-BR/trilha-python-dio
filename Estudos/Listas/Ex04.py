#4. Verifique se um nome está dentro da lista

nomes = ["ana", "joão", "carla"]
nome_procurado = input("Digite um nome: ")

if nome_procurado in nomes:
    print(f"{nome_procurado}, este nome está na lista!")
else:
    print(f"{nome_procurado}, não está na lista!")
