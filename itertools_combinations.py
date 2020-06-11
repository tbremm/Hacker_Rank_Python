# https://www.hackerrank.com/challenges/itertools-combinations/problem

from itertools import combinations

inp = list(input().split(' '))
s = sorted(inp[0])
n = int(inp[1])

for k in range(1, n + 1):
    print(*[''.join(i) for i in combinations(s, k)], sep='\n')
