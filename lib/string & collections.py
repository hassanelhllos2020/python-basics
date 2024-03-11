import string 
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.digits)
print(string.whitespace)
print(string.punctuation)
print("---------------")
import collections
pointe = collections.namedtuple("point", ['x','y','z'])
p1 = pointe(1,2,3)
print(p1)
print(p1[0])
print(p1.y)
