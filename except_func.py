import random

def raise_func():
    raise random.choice([KeyError, IndexError])

def except_func():
    try:
        random.choice([raise_func(), myexcept_raise_func()])
    except (KeyError, IndexError, MyException) :
        return "Got exception"
    else:
        return "No exception caught"

def myexcept_raise_func():
    raise MyException

class MyException(Exception):
    pass

