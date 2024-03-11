#with open("pi.txt", 'a') as pii:
#    pii.write("//")

with open("pi.txt") as pii:
    piii = pii.readlines() 
# readline returns a list of chars
#print(piii)  -> returns a list of lines
print(f"length: {len(piii)}")
n = 0
for i in piii:
    print(f"{n} : {i.strip()}")
    n+=1
