# MAKING CLASS BankAccount
# PRIVATE ATTRIBUTES ARE __account_holder and __balance
# METHODS ARE deposite(amount), withdraw(amount) AND get_balance()

class BankAccount:
    def __init__(self, acc_holder, balance):
        self.__account_holder = acc_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount 
        else:
            print("Deposite amount must be greater than 0")

    def withdraw(self, amount):
        if amount > 0:
            if amount < self.__balance:
                self.__balance -= amount
            else:
                print("Insufficient Balance")
        else:
            print("Withdraw amount must be greater than 0")

    def get_balance(self):
        print(f"Mr. {self.__account_holder} Your Current Balance is {self.__balance}")

acc1 = BankAccount("Mayuresh", 2000000) 
acc1.deposit(50000)
acc1.get_balance()  