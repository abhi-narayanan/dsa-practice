"""
Write a function that takes a non-negative integer and returns the largest integer whose square is less than or equal to the integer given.
Example -
Assume input integer is 300.
The expected output of the function should be 17, since 17^2 = 289.
Note that 18^2 = 324 > 300, so the number 17 is the correct response.
"""

k = 300

# 1 2 3 4 5 6 7 8 9 10 11 12

def integer_square_root(k):
    low = 1
    high = k

    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid

        if mid_squared <= k:
            low = mid + 1
        else:
            high = mid - 1
    return low - 1

print(integer_square_root(k))