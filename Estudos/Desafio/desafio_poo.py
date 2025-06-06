from abc import ABC, abstractmethod
from datetime import date
#----------------------------------------------------------------------
class Conta():
        def __init__(self,saldo=0.0,numero=0, agencia="None", cliente="None", historico=""):
            self._saldo = saldo
            self._numero = saldo
            self._agencia = agencia
            self._cliente = cliente
            self._historico = historico(Historico)

        def saldo(self):
              print(f"Seu saldo é de {self._saldo:.2f}")

        def nova_conta(self, cliente, numero):
              pass
        
        def sacar(self):
              pass

        def depositar(self):
              pass     
        

class ContaCorrente(Conta):
      
      def __init__(self, saldo=0, numero=0, agencia="None", cliente="None", historico="None", limite=0.0, saque_limite=0.0):
            super().__init__(saldo, numero, agencia, cliente, historico)
            self.limite= limite
            self.saque_limite= saque_limite
#----------------------------------------------------------------------
class Historico():
    def adicionar_transacao(transacao):
         pass
#-----------------------------------------------------------------------
class Transacao(ABC):
        
        def registrar():
              pass


class Sacar(Transacao):
      def __init__(self,valor):
            super().__init__()
            self.valor = valor
            
            def registrar(valor):
                  pass
                       
                    
class  Depositar(Transacao):
      def __init__(self,valor):
            super().__init__()
            self.valor = valor

            def registrar(valor):
                  pass

      
#----------------------------------------------------------------------
class Cliente():
        def __init__(self, endereco, contas):
              self.endereco = endereco
              self.contas = contas

        def realizar_transacao(self, conta, transacao(Transacao)):
              pass
        

        def adicionar_conta(self):
              pass

class PessoaFisica(Cliente):
       def __init__(self, endereco, contas, cpf, nome, data_nascimento= date.now()):
             super().__init__(endereco, contas)
             self.cpf = cpf
             self.nome = nome
             self.data_nascimento = data_nascimento

#----------------------------------------------------------------------
