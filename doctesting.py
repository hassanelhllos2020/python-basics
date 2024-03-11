def factorial(n) :
    """ returns the factorial of any number
        >>> factorial(5)
        120
        >>> factorial(-5)
        Traceback (most recent call last):
            ...
        ValueError: enter postive number
        >>> factorial(5.2)
        Traceback (most recent call last):
            ...
        ValueError: enter integer number
        """
    
    import math
    if n <=0 :
        raise ValueError("enter postive number")
    elif math.floor(n) != n :
        raise ValueError("enter integer number")
    else:
        result = 1
        for i in range(1,n):
            result *=  n
            n -= 1
        return result
        
#number = int(input("enter number: "))
#print(factorial(number))
#li = [factorial(l) for l in range(1,6)]
#print(li)
#print(factorial(5.2))
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)



    """ returns the factorial of any number
    >>>factorial(5)
    120
    >>>factorial(-5)
    Traceback (most recent call last):
        ...
    ValueError: enter postive number
    >>>factorial(5.2)
    Traceback (most recent call last):
        ...
    ValueError: enter integer number
    """