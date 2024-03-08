class account :
    def __init__ (self, name, balance) :
        self.name = name
        self.balance = balance
    def deposit(self, money) :
        if money > 0 :
            self.balance += money
        else:
            print("!!!!!enter postive value!!!!!")
    def withdraw(self, money) :
        if money >= 0 and money < self.balance:
            self.balance -= money
        else:
            print("!!!!!enter postive value!!!!!")
    


#acc1 = account(input("enter your bank accoount name: "), float(input("enter your balance: ")))
acc1 = account("hassan", 5000)
print(acc1.name, acc1.balance)
choose = 4
while choose == 1 or choose == 2 or choose == 4:
    choose = int(input("1-deposit \n2-withdraw \n3-exit: \n choose:"))
    if choose == 1 :
        d = float(input("enter amount of money you want to deposit: "))
        acc1.deposit(d)
        print(f"{d} added successfully ")

    elif  choose == 2:
        d = float(input("enter amount of money you want to withdraw: "))
        acc1.withdraw(d)
        print(f"{d} withdrawn successfully ")
    else: 
        break
    print("--------------------------operator overloading")
print(acc1.name, acc1.balance)
