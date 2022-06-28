class Account:
    def _init_(self, name):
        self.balance=0
        self.name = name

    print(" welcome , Your Account is Created.")

    def deposit(self):
        amount=int(input('Enter the amount to deposit:'))
        self.balance = amount
        print('Your New Balance = %d' %self.balance)

    def withdraw(self):
       amount=int(input('Enter the amount to withdraw:'))

       if(amount > self.balance):
        print('Insufficient Balance!')
       else:
        self.balance-=amount
       
        print('Your Remaining Balance = %d' %self.balance)
       

    def enquiry(self):
        print('Your Balance = %d' %self.balance)
        print('Thank for for banking with us')


account= Account()
account.deposit()
account.withdraw()
account.enquiry()