"""
Define a bitonic sequence as a sequence of integers such that:
x_1 <= ... <= x_k >= ... >= x_n-1 for some k, 0 <= k < n

For example -
1, 2, 3, 4, 5, 4, 3, 2, 1
is a bitonic sequence. Write a program to find the largest element in such a sequence. In the above example, the program should return 5
We assume that such a peak element exists.
"""

# Peak element is 5
A = [1, 2, 3, 4, 5, 4, 3, 2, 1]

# Peak element is 4
B = [1, 2, 3, 4, 1]

# Peak element is 6
C = [1, 6, 5, 4, 3, 2, 1]

def find_highest_number_binary(lst):
    highest_num = float("-inf")
    low = 0
    high = len(lst) - 1

    # Require atleast 3 elements for a valid bitonic seqeunce
    if len(lst) < 3:
        return None

    while low <= high:
        mid = (low + high) // 2
        mid_left = lst[mid - 1]
        mid_right = lst[mid + 1]

        if mid_left > mid_right:
            highest_num = max(highest_num, mid_left)
            high = mid - 1
        elif mid_left < mid_right:
            highest_num = max(highest_num, mid_right)
            low = mid + 1
        else:
            return lst[mid]

    return highest_num

print(find_highest_number_binary(A))
print(find_highest_number_binary(B))
print(find_highest_number_binary(C))