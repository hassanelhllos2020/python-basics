#def summ(a = 1,b = 1) :
#    """this function for adding 2 numbers"""
#    result = a - b 
#    return result

#print(summ(int(input("enter num1: ")),int(input("enter num2: "))))
#r = summ(b = 5, a = 10)
#summ?? 
print("--------------------------")
def average(*nums) :
    return sum(nums)
print( average(10,20,30) )
print("--------------------------map")
def square(n) :
    return n ** 2
li = [1,2,3,10]
re = map(square ,[1,2,3,10] )
print(list(re))
print("-------------------------- lambda")
f = lambda a,b,c : a + b - c + 10
print(f(1,2,3))