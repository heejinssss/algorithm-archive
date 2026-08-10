import math

def solution(array, n):

    """
    MIN_VALUE = array[0]

    for a in array:
        if abs(n-MIN_VALUE) > abs(n-a):
            MIN_VALUE = a
        elif abs(n-MIN_VALUE) == abs(n-a):
            MIN_VALUE = min(MIN_VALUE, a)

    return MIN_VALUE
    """

    array.sort(key=lambda x: (abs(x-n), x-n))
    
    return array[0]
