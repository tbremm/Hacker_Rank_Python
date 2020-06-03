# Lilah has a string, s, of lowercase English letters that she repeated infinitely many times. Given an integer, n,
# find and print the number of letter a's in the first n letters of Lilah's infinite string.
#
# For example, if the string s = 'abcac' and n = 10, the substring we consider is abcacabcac, the first n characters of
# her infinite string. There are 4 occurrences of a in the substring.
#
# Function Description
# Complete the repeatedString function in the editor below. It should return an integer representing the number of
# occurrences of a in the prefix of length n in the infinitely repeating string.
#
# repeatedString has the following parameter(s):
# s: a string to repeat
# n: the number of characters to consider
#
# Input Format
# The first line contains a single string, s.
# The second line contains an integer, n.
#
# Constraints
# 1 <= |s| <= 100
# 1 <= n <= 10^12
# For 25% of the test cases, n <= 10^6.
#
# Output Format
# Print a single integer denoting the number of letter a's in the first n letters of the infinite string created by
# repeating s infinitely many times. 


def repeatedString(s, n):
    # This is the discussion solution:
    return s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")

    # The following was my first attempt: (did basically the same as above, just did the counting myself)
    # sub_a = 0  # Total num of 'a' in s
    # mod_a = 0  # Num of 'a' in final piece of s at end of repetition
    # s_part = n % len(s)
    # for c in s[:s_part]:  # Get num of 'a' in final part of s repetition
    #     if c == 'a':
    #         mod_a += 1
    # for c in s:  # Get the number of a's in the string
    #     if c == 'a':
    #         sub_a += 1
    # return (sub_a * (n // len(s))) + mod_a


in_str = 'aba'  # abaabaabaa
repeat = 10
print(repeatedString(in_str, repeat))
