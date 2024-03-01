print("#------------------------------------#")
cars = {}

for index in range(0,2):
    msg = input("do you want to add more? ")
    if msg == 'yes' :
        cars[index] =  {'name':input("enter car : "),
                        'model':input("enter model: "),
                        'owner':input("enter owner: ")}
    else :
        print("\ndone\n")

print(cars)