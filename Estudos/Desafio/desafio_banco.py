
def menu():
    menu = """"Bem-vindo ao Sistema Bancário
               Selecione abaixo a função que deseja realizar
                1. Depositar
                2. Sacar
                3. Extrado Bancario
                4. Sair"""

    return menu

def depositar(saldo,deposito,extrato):
    saldo += float(deposito)
    extrato.append (f"Deposito no valor:       {deposito:.2f}")
    return saldo

def sacar (saldo, saque, extrato):
    if saque > saldo:
        print("Você não possui saldo o suficiente!")
    else:
        #saque = float(input("Qual o valor do saque:      "))
        saldo -= saque
        extrato.append (f"Saque no valor de {saque:.2f}") 
        return saldo, extrato

def mostrar_extrato(saldo,extrato):
        print("\n=== EXTRATO ===")
        
        if extrato:
            for item in extrato:
                print(item)
        else:
            print("Nenhuma movimentação.")
        
        print(f"\nSaldo atual: R$ {saldo:.2f}")
         

def main():
    saldo =1000.0
    deposito= 0.0
    saque_limite= 500.00
    limite_saque_diario = 0
    extrato=[]
    saque = 0.0
   
    
    while True:
        print(menu())
        op = int(input ("Selecione uma opção:   "))

        if op == 1:
            deposito = float(input ("Valor a ser depositado:  "))
            if deposito >0:    
                
                saldo = float(depositar(saldo,deposito,extrato))
            else:
                print ("Somente números positivos!")    

        elif op == 2:
                
                if limite_saque_diario < 3:
                        saque = float(input ("Quanto deseja sacar?"))
                        if saque < saque_limite:
                            sacar(saldo,saque,extrato)

                            print (f"Você realizou o saque de {saque:.2F}")
                            limite_saque_diario += 1
                        else:
                            print("O limite de saque é 500,00 reais")

                else:
                     print("O limite maximo de saque é 3 vezes por dia.") 
                          
        elif op == 3:
             mostrar_extrato(saldo,extrato)

        elif op == 4:
             print("Obrigado por usar nosso sistema!")
             break
        else:
             print("Opção inválida!")   
                


main()
    
