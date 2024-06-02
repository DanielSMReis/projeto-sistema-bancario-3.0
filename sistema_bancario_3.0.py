from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar Usuario
[c] Criar conta
[q] Sair

=> """

"""
LIMITE_SAQUES = 3
AGENCIA = "0001"

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuarios = []
contas = []
numero_conta = 0
"""
class Transacao:
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
        
#----------------------------------------------------------

def extratar(extrato, saldo = saldo):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)  # noqa: E999
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    return


def validar_usuario(cpf, usuarios):
    cpf = cpf
    usuarios = usuarios
    for usuarios in usuarios:
        if usuarios["cpf"] == cpf:
            return False
        else:
            return True


def mk_user(usuarios):
    nome = input("digite o nome do usuario: ")
    data_de_nascimento = input("digite a data de nascimento (dd-mm-aaaa): ")
    cpf = input("digite o cpf do usuario: ")
    endereco = input("digite o endereço do usuario (logradouro, numero - bairro - cidade/sigla estado): ")

    if (nome and data_de_nascimento and cpf and endereco):
        user_valido = validar_usuario(cpf, usuarios)
        if user_valido:
            usuarios.append({"nome": nome, "data_de_nascimento": data_de_nascimento,"cpf": cpf, "endereco": endereco})
            
        else:
            print("Usuario ja possue cadastro!")

    else:
        print("Usuário invalido, favor preencher todos os campos")


def mk_acc(AGENCIA, numero_conta, usuarios):
    nw_acc = input("digite o numero do cpf do usuario para ser vinculado à conta: ")
    for usuarios in usuarios:
        if usuarios["cpf"] == nw_acc:
            numero_conta += numero_conta

        else:
            print("CPF de usuario ainda nao cadastrado!")
    contas.append({"agencia": AGENCIA, "Conta": numero_conta, "CPF": nw_acc})
    

while True:

    opcao = input(menu)

    if opcao == "d":
       extrato,saldo = depositar(extrato,saldo)

    elif opcao == "s":
        extrato, saldo, numero_saques = sacar(extrato, saldo, numero_saques, LIMITE_SAQUES)

    elif opcao == "e":
        extratar(extrato, saldo)

    elif opcao == "u":
        mk_user(usuarios)
    
    elif opcao == "c":
        mk_acc(AGENCIA, numero_conta, usuarios)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

