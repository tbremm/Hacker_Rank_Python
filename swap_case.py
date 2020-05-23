# You are given a string and your task is to swap cases.
# In other words, convert all lowercase letters to uppercase letters and vice versa.
#
# For Example:
#
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2
#
# Input Format
# A single line containing a string S.
#
# Constraints
# - < len(S) <= 1000
#
# Output Format
# Print the modified string S.


def swap_case(s):
    swapped = []
    for c in s:
        if c.islower():
            swapped.append(c.upper())
        else:
            swapped.append(c.lower())
    out_s = ''.join(swapped)
    return out_s


s = input()
result = swap_case(s)
print(result)

