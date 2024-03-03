text = ('this is sample text with several words '
        'this is more sample text with some different words '
        'that is also another text with other different words'
       )
count ={}
for i in text.split(" ") :
    if i not in count :
        count[i] = 1
    else:
        count[i] +=1

for v,n in sorted(count.items()) :
    print( f"{v:<10} --> {n}" )

