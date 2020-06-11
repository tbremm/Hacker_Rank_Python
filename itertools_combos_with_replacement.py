# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

from itertools import combinations_with_replacement

inp = list(input().split(' '))
s = sorted(inp[0])
k = int(inp[1])

print(*[''.join(i) for i in combinations_with_replacement(s, k)], sep='\n')
