# 5. Adicione 3 números digitados pelo usuário em uma lista e depois imprima a lista
# # Dica: use input() dentro de um laço e .append() na lista

lista = []

for i in range(3):
     numero = int (input("Digite um numero: "))
     lista.append(numero)

print(lista)     
