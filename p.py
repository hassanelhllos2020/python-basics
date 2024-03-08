    # capital: 65 to 90
    #small: 97 to 122

"""print(chr(70)) # 70 - 65 = 5
print(chr(5+97)) 
print(ord("f"))
"""
def swap(txt) :
    newtxt = []
    for i in range(len(txt)) :
        if 97 <= ord(txt[i]) <= 122:
          litter = chr(ord(txt[i]) - 32 )
        elif 65 <= ord(txt[i]) <= 90 :
            litter = chr(ord(txt[i]) + 32 )
        else:
            newtxt.append(txt[i])
            continue
    
        newtxt.append(litter)
    newtxt ="".join(newtxt)
    return newtxt
txt = input("enter text: ")
print(swap(txt))
