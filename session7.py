import random

# DOC String Check
def docstring_check(fn):
    """
    This function is used to check the docstring count for each function, it checks if 
    the doc string is of minimum 50 characters
    """
    min_count = 50

    def count():
        """
        This function returns True, if the docstring has minimum 
        50 characters else it returns false.
        """
        nonlocal min_count
        doc_string = fn.__doc__
        if doc_string and len(doc_string) >= min_count:
            return True
        else:
            return False
    return count

# Next Fibonacci
def fib():
    """
    Function to generate next fibonacci numbeer

    """
    first = 0
    second = 1
    def gen_next_number():
        """
        This function sums the previous two numbers and returns the generated sum, it also updates the previous
        two numbers with the new value
        """
        nonlocal first,second
        temp = second
        second = first + second
        first = temp
        return second
    return gen_next_number

# Function call counter
def add(a, b):
    """
        This function is used to add two numbers
            a:  Number 1
            b:  Number 2
    """
    return a + b

def mul(a, b):
    """
        This function is used to multiply two numbers
            a: Number 1
            b: Number 2
    """
    return a*b

def div(a, b):
    """
        This function is used to multiply two numbers
            a: Number 1
            b: Number 2
    """
    if b == 0:
        raise ValueError("Zero divison Error")
    return a/b


def counter(fn):
    """
        This function is used to calculate the number of times a function is being called.
    """
    count = 0
    def inner(*args,**kwargs):
        """
            This function updates the counter and returns it.
        """
        nonlocal count
        count += 1
        return count
    return inner

count_dict = {'add':0,'mul':0,'div':0}


def count_with_global_dict(fn):
    """
        This function is used to calculate the number of times a function is being called.
    """
    count = count_dict[fn.__name__]
    def inner(a,b):
        """
            This function updates the counter and returns it.
        """
        nonlocal count
        count += 1
        count_dict[fn.__name__] = count
        return count
    return inner

def count_with_user_dict(fn, count_dict2):
    """
        This function is used to calculate the number of times a function is being called and update the dictionary
        which is passed as a parameter.

    """
    count = count_dict2[fn.__name__]
    def inner(a,b):
        """
            This function updates the counter and returns it.
        """
        nonlocal count
        count += 1
        count_dict2[fn.__name__] = count
        return count
    return inner
