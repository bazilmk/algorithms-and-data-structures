'''
Author: Bazil Muzaffar Kotriwala
Timestamp: 19-Dec-2016 4:55PM
'''

def factorial(n):
    '''
    This program calculates the factorial of any number tail recursively
    :param n: Number inputted by the user
    :precondition: The number cannot be negative
    :postcondition: The factorial of the number is calculated
    :return: The factorial of the number
    :complexity: Best Case = Worst Case = O(n), where n is the number of times the recursive call is made
    '''

    return factorial_aux(n,1)

def factorial_aux(n, result):
    if n == 0:
        return result
    else:
        return factorial_aux(n-1, result * n)