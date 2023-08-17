# operations.py

def withdraw(*, balance, amount, statement, limit, num_withdrawals, withdrawal_limit):
    if balance >= amount and num_withdrawals < withdrawal_limit and amount <= limit:
        balance -= amount
        statement.append(f'Saque: R$ {amount:.2f}')
        num_withdrawals += 1
    return balance, statement

def deposit(balance, amount, statement):
    if amount > 0:
        balance += amount
        statement.append(f'Depósito: R$ {amount:.2f}')
    return balance, statement

def statement(balance, *, statement):
    if not statement:
        return 'Não foram realizadas movimentações.'
    else:
        result = 'Extrato:\n'
        for transaction in statement:
            result += transaction + '\n'
        result += f'Saldo Atual: R$ {balance:.2f}'
        return result
