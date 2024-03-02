grade = int(input("enter your grade: "))
if grade >= 90 :
    print("A")
elif grade >= 80 :
    print("B")
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
else:
    print('F')
print("------------------Conditional Expressions")
result = 'passed' if grade >= 60 else 'failed'
print(result)
typ = 'even' if grade % 2 == 0 else 'odd'
print(typ)
print("------------------Conditional Expressions neted if")
result2 = 'a' if grade >= 90 else ('b' if grade >= 80 else ('c' if grade >= 70 else ('d' if grade >= 60 else 'f')))
print(result2)
print("-----------------------")
l = [i for i in range(1,11)]
print(l)
ll = [(i*10 if i % 2 == 0 else i) for i in range(1,11)]
print(ll)