class Banco:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')

    def saque(self, valor):
        if self.saldo >= valor and len(self.saques) < 3 and valor <= 500:
            self.saldo -= valor
            self.saques.append(valor)
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
        elif self.saldo < valor:
            print('Saldo insuficiente para realizar o saque.')
        elif len(self.saques) >= 3:
            print('Limite máximo de saques diários atingido.')
        elif valor > 500:
            print('Valor de saque excede o limite máximo de R$ 500.00.')

    def extrato(self):
        if not self.depositos and not self.saques:
            print('Não foram realizadas movimentações.')
        else:
            print('Extrato:')
            for deposito in self.depositos:
                print(f'Depósito: R$ {deposito:.2f}')
            for saque in self.saques:
                print(f'Saque: R$ {saque:.2f}')
            print(f'Saldo Atual: R$ {self.saldo:.2f}')


def main():
    banco = Banco()

    while True:
        print('1 - Depósito')
        print('2 - Saque')
        print('3 - Extrato')
        print('4 - Sair')

        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
            valor = float(input('Digite o valor do depósito: '))
            banco.deposito(valor)
        elif opcao == 2:
            valor = float(input('Digite o valor do saque: '))
            banco.saque(valor)
        elif opcao == 3:
            banco.extrato()
        elif opcao == 4:
            print('Saindo...')
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
    main()
