class BankAccount:
    def __init__(self):
        self.__balance = 150

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"На счет добавлено {amount} единиц. Баланс: {self.__balance}"
        else:
            return "Сумма пополнения должна быть положительной"

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Со счета снято {amount} единиц. Баланс: {self.__balance}"
        else:
            return "Недостаточно средств или сумма снятия некорректна"

account = BankAccount()

print(account.deposit(1000))
print(account.withdraw(100))