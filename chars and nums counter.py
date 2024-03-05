#for i in range(65,122):
#    print(i, chr(i))
# 65 to 90 capitale litters
# 97 to 122 small litters
# 48 to 57 numbers
name = input("enter your name: ")
chars = 0
numbers = 0
for n in list(name) :
    if 90 >= ord(n) >= 65 or 122 >= ord(n) >= 97 :
     chars += 1
    elif 48 <= ord(n) <= 57:
       numbers += 1
if numbers >= 1 :
   print("please enter vaild name without numbers")
else:
   print(f"hello mr {name}")
print(f"{chars} characters")
print(f"{numbers} numbers")

all_chars = [chr(c) for c in range(65,91)] + [chr(c) for c in range(97,123)]
print(all_chars)