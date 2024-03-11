try:
    5/0
except Exception as e:
    print(f"erorr: {e}")
    print(f"class: {e.__class__}")
    
print("------------------")
try:
    print(a)
    #print(5/0)
    #print("hello")
except NameError:
    print("name erorr")
except ZeroDivisionError :
    print("zero erorr")
else:   #print if no erorrs happend
    print("no erorrs")
finally: #print anyways
    print("done")
print("------------------")
try:
    raise Exception("erorr")
except Exception as ee:
    print("i raised the exception myself")
