from abc import ABC, abstractclassmethod


class Transacao(ABC):
    @property
    def valor(self):
        pass
    @abstractclassmethod
    def registrar(self, conta):
        pass


class Conta:

    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
        self.numero_saques = 0
        self.limite = 500
        self.LIMITE_SAQUES = 3
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar (self, valor, limite,numero_saques, LIMITE_SAQUES):
        saldo = self.saldo
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
           
        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            print("saque realizado com sucesso!")
            return True
        
        else:
            print("Operação falhou! O valor informado é inválido.")
            return False
    
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Deposito realizado com sucesso!")
            return True
        else:
            print("Operação falhou! O valor informado é inválido.")
            return False
    
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, LIMITE_SAQUES, limite, numero_saques):
        super().__init__(numero, cliente,LIMITE_SAQUES, limite, numero_saques)
    def sacar(self, valor):
        saque = Conta.sacar(valor)
    
    def depositar(self, valor):
        deposito = Conta.depositar(valor)
        
class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes


class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self,conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        
