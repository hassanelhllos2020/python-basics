import os
a = int(input("how many file you want to create: "))
for i in range(1,a+1): 
    os.system(f"mkdir file{i} ")