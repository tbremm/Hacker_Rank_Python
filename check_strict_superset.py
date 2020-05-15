# You are given a set A and n other sets.
# Your job is to find whether set A is a strict superset of each of the n sets.
# Print True, if A is a strict superset of each of the n sets. Otherwise, print False.
# A strict superset has at least one element that does not exist in its subset.
#
# Example
# Set ([1,3,4]) is a strict superset of set ([1,3]).
# Set ([1,3,4]) is not a strict superset of set ([1,3,4]).
# Set ([1,3,4]) is not a strict superset of set ([1,3,5]).
#
# Input Format
# The first line contains the space separated elements of set A.
# The second line contains integer n, the number of other sets.
# The next n lines contains the space separated elements of the other sets.
#
# Constraints
# 0 < len(set(A)) < 501
# 0 < n < 21
# 0 < len(other sets) < 101
#
# Output Format
#
# Print True if set A is a strict superset of all other n sets. Otherwise, print False.

a = set(map(int, input().split()))
n = int(input())
is_superset = True
for i in range(n):
    new_set = set(map(int, input().split()))
    if not a.issuperset(new_set):
        is_superset = False
        break
print(is_superset)
