def sum_array(array):
    total=0
    for i in array:
        total+=i

    '''Return sum of all items in array'''
    return total

def fibonacci(n):
    if n<=1:
        return n
    else:
        fib_number=fibonacci(n-1)+fibonacci(n-2)

    '''Return nth term in fibonacci sequence'''
    return fib_number

def factorial(n):
    if n<2:
        return 1
    else:
        fact_number=n*factorial(n-1)

    '''Return n!'''
    return fact_number

def reverse(word):
    word=word[::-1]

    '''Return word in reverse'''
    return word        
