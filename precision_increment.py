"""
Arbitrary Precision Increment
An array of non-negative digits that represent a decimal
Add one to the integer. Assume the solution still works even if implemented in a language with finite-precision arithmetic
A = [1, 4, 9]
=> Add 1 - [1, 5, 0]
"""

A = [9, 9, 9, 9]

# s = "".join(map(str, A))
# print(s)

def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A

print(plus_one(A))