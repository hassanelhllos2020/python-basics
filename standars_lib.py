import os
#print("\n".join(os.listdir()))
#os.system("mkdir test")
#os.system("rm -rf test")
print(os.getcwd())
import glob
#print(glob.glob('*.py'))
from datetime import date
print(date.today())
print(date.today().strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
import random
print( random.randrange(1,100) )
print( random.randint(1,5) )
print( random.choice(["win", 'lose']) )
ls = [1,2,3,4,5,6,7,8,9,10]
print(ls)
random.shuffle(ls)
print(ls)
print(random.sample(['a','b','c','d','e'],k=2))
