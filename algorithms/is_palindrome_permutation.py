"""
Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or a phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
"""

palin_perm = "Tact Coa" # Taco Cat
not_palin_perm = "This is not a palindrome permutation"

# Time Complexity: O(n)
# Space Complexity: O(n)
def is_palindrome_permutation(input_str):
    input_str = input_str.replace(" ", "")
    input_str = input_str.lower()

    ht = dict()

    for i in input_str:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1

    odd_count = 0
    for _, v in ht.items():
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif v % 2 != 0 and odd_count != 0:
            return False
    return True

print(is_palindrome_permutation(palin_perm))
print(is_palindrome_permutation(not_palin_perm))