# https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations

inp = list(input().split(' '))
s = sorted(inp[0])
n = int(inp[1])
print(*[''.join(i) for i in permutations(s, n)], sep='\n')
