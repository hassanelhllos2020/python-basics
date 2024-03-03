c = 10
a = []
while c > 0 :
     if c % 2 != 0 : 
          c-= 1
          a.append(c)
          continue
     else:
        print(c)
        c-= 1
print(sorted(a))
print("-----------------------") #-----------------
l = ['pizza', 'mango', 'burger', 'friedchicken']
ll = []
while len(l) > 0 :
    print(l[-1])
    ll.append(l.pop())
print(ll)
print("#-----------------------#") #-----------------
birth = input("enter your birthday: ")
attemps = 0
while not birth.isdigit():
    attemps += 1
    birth = input("enter your birthday: ")
else:
    if attemps >=3 :
          print('rbna ehdehk')
    print(f"your age is {2024 - int(birth)} ")
