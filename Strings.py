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
print("...-----------------...")
print(f"zeros: {55:03}")
print(f'float: {22.33445:.4f} ' )
print(f'decimal left: {22:>5d} ' )
print(f'decimal right:{22:<5d} ' )
print(f'grouping digits:  {100000:,d} ' )
print(f'chr: {78:c}')
print("------------------Character Checks")
print( '27'.isdigit() )
print( 'a27'.isalnum() )

#
print("#--------------------------#")
#msg = "hello mr {n}, your age is {age} ".format(n = input("enter your name: "),age = 2024 - int(input("enter your birthday: ")))
#print(msg)
#
n = input("enter your name: ")
age = 2024 - int(input("enter your birthday: "))
#msg = "hello mr {}, your age is {} ".format(n,age)
msg = f"hello mr {n}, your age is {age} "
print(msg) 