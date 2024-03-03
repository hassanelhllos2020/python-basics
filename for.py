food = {
    'american':['pizza', 'mango', 'burger', 'friedchicken'],
    'egyptian': ['hawashy', 'kreb', 'molo5ya']    ,
    'drinks': ['cola', 'pepsi', 'sprite'],
        }
#print(food['american'])
for meal in food.keys():
    print( f"\n{meal}:" )
    for mel in food[meal] :
        print(mel, end=", ")
print("\n")        
foods_dictionary = {
    '1': 'foul',
    '2': 'falafel',
    '3': 'batates',
    '4': 'pickles',
    '5': 'koshary',
    '6': 'betengan'
}
#print( list(enumerate(foods_dictionary.items())) )

for c, (index, mell) in enumerate(foods_dictionary.items()) :
   print(c, index, mell)
print("---------------------------")
for r in range(1,11) :
    if r % 2 ==0 :
        print(f"{r} is even")
    else: 
        print(f"{r} is odd")
    