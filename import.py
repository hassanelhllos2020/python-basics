
class test:
    def __init__(self):
        pass
from swapcase import textmanp
#built-in modules , current wd, sys.path
txte = textmanp("test")
print(type(textmanp))
print(type(textmanp.swap))
print(f"the current module name is {__name__}")
print(test)
#print(dir(textmanp.swap))
import os
print(dir())
print(os.__file__)
print(os.__doc__)