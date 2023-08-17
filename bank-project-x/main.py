# main.py
from functions.users import User
from functions.accounts import Account
from functions.operations import withdraw, deposit, statement

def create_user():
    name = input('Digite o nome do usuário: ')
    birth_date = input('Digite a data de nascimento (dd/mm/aaaa): ')
    cpf = input('Digite o CPF (apenas números): ')
    address = input('Digite o endereço no formato: logradouro, numero - bairro - cidade/sigla estado: ')
    return User(name, birth_date, cpf, address)

def create_account(user):
     return Account(user)

def main():
    users = []
    accounts = []

    while True:
        print('1 - Criar Usuário')
        print('2 - Criar Conta Corrente')
        print('3 - Realizar Depósito')
        print('4 - Realizar Saque')
        print('5 - Visualizar Extrato')
        print('6 - Sair')

        option = int(input('Escolha uma opção: '))

        if option == 1:
            user = create_user()
            if not any(u.cpf == user.cpf for u in users):
                users.append(user)
                print('Usuário criado com sucesso.')
            else:
                print('Usuário com CPF já cadastrado.')

        elif option == 2:
            cpf = input('Digite o CPF do usuário: ')
            user = next((u for u in users if u.cpf == cpf), None)
            if user:
                account = create_account(user)
                accounts.append(account)
                print(f'Conta corrente criada com sucesso. Número da conta: {account.number}')
            else:
                print('Usuário não encontrado.')

        elif option == 3:
            account_number = int(input('Digite o número da conta: '))
            account = next((c for c in accounts if c.number == account_number), None)
            if account:
                value = float(input('Digite o valor do depósito: '))
                account.balance, account.deposits = deposit(account.balance, value, account.deposits)
                print(f'Depósito de R$ {value:.2f} realizado com sucesso.')
            else:
                print('Conta não encontrada.')

        elif option == 4:
            account_number = int(input('Digite o número da conta: '))
            account = next((c for c in accounts if c.number == account_number), None)
            if account:
                value = float(input('Digite o valor do saque: '))
                account.balance, account.withdraws = withdraw(balance=account.balance, amount=value, statement=account.withdrawals, limit=500, num_withdrawals=len(account.withdrawals), withdrawal_limit=3)
                print(f'Saque de R$ {value:.2f} realizado com sucesso.')
            else:
                print('Conta não encontrada.')

        elif option == 5:
            account_number = int(input('Digite o número da conta: '))
            account = next((c for c in accounts if c.number == account_number), None)
            if account:
                print(statement(account.balance, statement=account.deposits + account.withdrawals))
            else:
                print('Conta não encontrada.')


        elif option == 6:
            print('Saindo...')
            break

        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
    main()
