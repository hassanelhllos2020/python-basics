human = {
    'height': 170,
    'weight' :70,
    'eye-color': 'brown',
    'language': 'arabic',
}
print(human)
print("----------")
print(human.items())
print("----------")
print(human.keys())
print(human.values())
print("---------- edit")
human['height'] = 180
print(list(human.values()))
print("---------- add")
human['sex'] = 'male'
print(human)
print("---------- delete")
del human['sex'] 
print(human)
print("-----------------------------")
human2 = {
    'height': 200,
    'weight' :100,
    'eye-color': 'red',
    'language': ['arabic','english'],
}
print(human2['language'][1])
print("-----------------------------")
human4 = {'name':'ahmed','age':45,'language':['arabic','english'], 19:range(1,6)}
print(list(human4[19]))
print("---------------------nested ")
human0 = {'name':'mona', 'sex':'female', 'age':30}
humans = {
    1: {'name':'ahmed', 'sex':'male', 'age':19},
    2: {'name':'ali', 'sex':'male', 'age':22},
    3: human0
}
print(humans[3])
print(humans[1]['name'], humans[2]['name'], humans[3]['name'])
humans[3]['height'] = 50
print(humans[3])
print("#------------------------------------#")
humans[4] = {'name':input("enter name: ")}
humank = input("enter key: ")
humans[4][humank] = input("enter value: ")
print(humans)