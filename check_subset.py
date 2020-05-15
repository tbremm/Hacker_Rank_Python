# You are given two sets, A and B. (my comment - sets only hold unique values)
# Your job is to find whether set A is a subset of set B.
# If set A is subset of set B, print True.
# If set A is not a subset of set B, print False.
#
# Input Format
# The first line will contain the number of test cases, T.
# The first line of each test case contains the number of elements in set A.
# The second line of each test case contains the space separated elements of set A.
# The third line of each test case contains the number of elements in set B.
# The fourth line of each test case contains the space separated elements of set B.
#
# Constraints
# 0 < T < 21
# 0 < Num elements in each set < 1001
#
# Output Format
# Output True or False for each test case on separate lines.

num_tests = int(input())
for _ in range(num_tests):  # Loop through and get all the input
    len_a = int(input())
    a = set(map(int, input().split()))
    _ = int(input())
    b = set(map(int, input().split()))

    # Just do the work while gathering inputs to save space complexity of storing all the lists at once
    print(a.issubset(b))
