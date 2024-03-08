    # capital: 65 to 90
    #small: 97 to 122

"""print(chr(70)) # 70 - 65 = 5
print(chr(5+97)) 
print(ord("f"))
"""
class textmanp:
    def __init__(self,txt) :
       self.txt = txt

    def swap(self) :
        self.newtxt = []
        for i in range(len(self.txt)) :
            if 97 <= ord(self.txt[i]) <= 122:
                self.litter = chr(ord(self.txt[i]) - 32 )
            elif 65 <= ord(self.txt[i]) <= 90 :
                self.litter = chr(ord(self.txt[i]) + 32 )
            else:
                self.newtxt.append(self.txt[i])
                continue
        
            self.newtxt.append(self.litter)
        self.newtxt ="".join(self.newtxt)
        return self.newtxt
txt = textmanp(input("enter text: "))
print(txt.swap())
