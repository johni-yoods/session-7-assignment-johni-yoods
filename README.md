# Closures

## Session 8

#### DOC String Check


This function is used to check the docstring count for each function, it checks if the doc string is of minimum 50 characters.

#### def count():
        nonlocal min_count
        doc_string = fn.__doc__
        if doc_string and len(doc_string) >= min_count:
            return True
        else:
            return False

####  Next Fibonacci

 Function to generate next fibonacci numbeer. This function sums the previous two numbers and returns the generated sum, it also updates the previous two numbers with the new value
 #### def gen_next_number():

        nonlocal first,second
        temp = second
        second = first + second
        first = temp
        return second
    return gen_next_number

#### Function call counter

This function is used to calculate the number of times a function is being called.
#### def inner(*args,**kwargs):

        nonlocal count
        count += 1
        return count
    return inne
#### Count the function call and store  in dict
 This function is used to calculate the number of times a function is being called
#### def inner(a,b):
        nonlocal count
        count += 1
        count_dict[fn.__name__] = count
        return count
    return inner

#### count_with_user_dict
This function is used to calculate the number of times a function is being called and update the dictionary which is passed as a parameter.
#### def inner(a,b):
        nonlocal count
        count += 1
        count_dict2[fn.__name__] = count
        return count
    return inner


