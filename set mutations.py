# TASK
# You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation
# operations on set A.
#
# Your task is to execute those operations and print the sum of elements from set A.
#
# Input Format
# The first line contains the number of elements in set A.
# The second line contains the space separated list of elements in set A.
# The third line contains integer N, the number of other sets.
# The next 2*N lines are divided into N parts containing two lines each.
# The first line of each part contains the space separated entries of the operation name and the length of the other
# set.
# The second line of each part contains space separated list of elements in the other set.
#
# Constraints
# 0 < len(set(A)) < 1000
# 0 < len(otherSets) < 100
# 0 < N < 100
#
# Output Format
# Output the sum of elements in set A.

num_a = int(input())
a = set(map(int, input().split()))
n = int(input())
ops = []
sets = []
for i in range(n):
    ops.append(input().split()[0])  # operation, who cares about the len of the set
    sets.append(set(map(int, input().split())))

# num_a = 16
# a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 24, 52}
# n = 4
# ops = ['intersection_update', 'update', 'symmetric_difference_update', 'difference_update']
# sets = [{2, 3, 5, 6, 8, 9, 1, 4, 7, 11}, {55, 66}, {22, 7, 35, 62, 58}, {11, 22, 35, 55, 58, 62, 66}]

for i, op in enumerate(ops):
    if op.lower() == 'intersection_update':
        a.intersection_update(sets[i])
    elif op.lower() == 'update':
        a.update(sets[i])
    elif op.lower() == 'symmetric_difference_update':
        a.symmetric_difference_update(sets[i])
    elif op.lower() == 'difference_update':
        a.difference_update(sets[i])

print(sum(a))
