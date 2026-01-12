"""
Given 2 numbers, find their product using recursion
"""
x = 500
y = 3000

def recursive_product(x, y):

    # This cuts down on the total number of recursive calls
    if x < y:
        return recursive_product(y, x)
    if y == 0:
        return 0
    return x + recursive_product(x, y-1)

print(recursive_product(x, y))