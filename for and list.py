a = []
for i in range(0,5) : 
    inn1 = input("enter car: ")
    a.append(inn1)
print("note!!!! if your enterd honda it will be deleted ")
print(a)
a.remove("honda")
first_car = a.pop(0)
del a[-1]
print("\n my first car is: " + first_car)
print("i delted my last car:- ")
print(a)
#sum function