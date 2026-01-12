"""
Given a string, find the first upper case character
Solve using both iterative and recursive solution
"""
input_1 = "lucidProgramming"
input_2 = "LucidProgramming"
input_3 = "lucidprogramming"

def find_uppercase_iterative(input_str):
    for i in range(len(input_str)):
        if input_str[i].isupper():
            return input_str[i]
    return "No uppercase character found!"

def find_uppercase_recurive(input_str, idx=0):
    if input_str[idx].isupper():
        return input_str[idx]
    if idx == len(input_str) - 1:
        return "No uppercase character found!"
    return find_uppercase_recurive(input_str, idx+1)

print(find_uppercase_iterative(input_1))
print(find_uppercase_iterative(input_2))
print(find_uppercase_iterative(input_3))

print(find_uppercase_recurive(input_1))
print(find_uppercase_recurive(input_2))
print(find_uppercase_recurive(input_3))