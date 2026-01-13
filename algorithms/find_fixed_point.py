"""
A fixed point in an array A is an index i such that A[i] is equal to i.
Given an array of n distinct integers sorted in ascending order, write a function that returns a fixed point in the array. If there is no fixed point return None
"""

# Fixed point is 3
A = [-10, -5, 0, 3, 7]

# Fixed point is 0
B = [0, 2, 5, 8, 17]

# No Fixed point, return None
C = [-10, -5, 3, 4, 7, 9]

# Time Complexity: O(n)
# Space Complexity: O(1)
def find_fixed_point_linear(A):
    for i in range(len(A)):
        if A[i] == i:
            return A[i]
    return None

# Time Complexity: O(n)
# Space Complexity: O(1)
def find_fixed_point_binary(A):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) // 2

        if mid > A[mid]:
            low = mid + 1
        elif mid < A[mid]:
            high = mid - 1
        else:
            return A[mid]     
    return None

print(find_fixed_point_binary(A))
print(find_fixed_point_binary(B))
print(find_fixed_point_binary(C))