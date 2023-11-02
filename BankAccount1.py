class BankAccount:
    def __init__(self, n, ac, b):
        self.__name = n
        self.__accountnumber = ac
        self.__balance = b


    # Methods to adjust balance
    def deposit(self, amt):
        self.__balance += amt

    def withdraw(self, amt):
        if self.__balance >= amt:
            self.__balance -= amt
        else:
            print('Insufficient funds')

    def __str__(self):
        return f'Account Information:\n\tName: {self.__name}, Account Number: {self.__accountnumber}, Balance: ${self.__balance:,.2f}'

def main():
    n = input("Enter Name: ")
    ac = int(input('Enter account number: '))
    b = float(input('Enter initial balance: '))
    acc1 = BankAccount(n, ac, b)
    print(acc1)
    depositing = acc1.deposit(int(input("enter depositing account amount")))
    print(depositing)
    print(acc1)
    withdrawing = acc1.withdraw(int(input("enter withdrawing account amount")))
    print(withdrawing)
    print(acc1)
    # setnm = input('Enter new name: ')
    # acc1.setname(setnm)
    # print(acc1)

if __name__ == "__main__":
    main()
