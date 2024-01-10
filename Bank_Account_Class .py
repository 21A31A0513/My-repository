class  bankAccount:
    def __init__(self,name,Anumber,balance):
        self.name=name
        self.Anumber=Anumber
        self.currentbalance=balance
    def deposit(self,amount):
        self.currentbalance+=amount
    def withdraw(self,amount):
        if amount>self.currentbalance:
            print("insufficient balance")
        else:
            self.currentbalance-=amount
    def display(self):
        print(self.currentbalance) 
name=input("Enter Account holder name :")
Anumber=int(input("Enter Account Number : "))
balance=int(input("Enter balance in the account:"))
obj=bankAccount(name,Anumber,balance)
while(1):
    print("1.deposit cash  2.withdraw cash   3.display current balance  4.exit")
    ch=int(input("Enter your choice : "))
    if ch==1:
        n=int(input("Enter amount:"))
        obj.deposit(n)
    elif ch==2:
        n=int(input("Enter amount:"))
        obj.withdraw(n)
    elif ch==3:
        obj.display()
    else:
        break
