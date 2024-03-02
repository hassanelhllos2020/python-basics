#format()
a = "my name is {} and i'm {} years old".format('hassan', 22)
print(a)
print("-----------")
# replacement fields with keyword arguments
a = "my name is {b} and i'm {a} years old".format(a='hassan', b=22)
print(a)
print("-----------")
b = "hi my name is {a} and i'm working as an {job[0]}"
print(b.format(a = 'hassan', job = ['eng', 'doctor']))
print("--------------------------")
nn = 'ahmed'
agee = 22
print(f"my name is {nn} and i'm {agee} years old")
print("--------------------------split")
name = "ahme - mohamed - ali, reda"
print(name.split("-"))
print("--------------------------splitline")
lines = """ this is line 1
line 2"""
print(lines.splitlines())
print("--------------------------join")
m = ['one','tow','three']
print( " - ".join(m) )
print("--------------------------partition")
mn = "ahmed : 19 years old - married "
print(mn.partition(":"))
print("#--------------------------#")
#
#msg = "hello mr {n}, your age is {age} ".format(n = input("enter your name: "),age = 2024 - int(input("enter your birthday: ")))
#print(msg)
#
n = input("enter your name: ")
age = 2024 - int(input("enter your birthday: "))
msg = "hello mr {}, your age is {} ".format(n,age)
print(msg)