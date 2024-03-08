class dog:
    
    def __init__ (self, name): #dunder 
        self.name = name
        print('init')
    type = "german"
    def bark(self) :
        print("haw haw haw")
        

dog1 = dog('rex')
#dog2 = dog(input("enter your dog name: "))
dog1.age = "6"
dog1
print(dog1.name)
print(dog1.type)
#print(dog2.name)
dog1.bark()
print("-----------------------")
class account:
    def __init__ (self, name, balance):
        self.name = name
        self.balance = balance
    def __repr__ (self) :
        return f"{self.name} has {self.balance} in his account"
    def __add__(self,other) :
        return f"{self.name} and {other.name} has a total amount of {self.balance + other.balance}"

acc1 = account('hassan', 900)
acc2 = account('ahmed', 500)

print(acc1.name, acc1.balance)
print(acc2.name, acc2.balance)
print("-------------------------")
print(acc1)
print(acc1 + acc2)