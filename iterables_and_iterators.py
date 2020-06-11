# https://www.hackerrank.com/challenges/iterables-and-iterators/problem

from itertools import combinations


def get_probability(string, num_indicies, char):
    combos = list(combinations(string, num_indicies))
    num_char = 0
    for combo in combos:
        if char in combo:
            num_char += 1
    return num_char / len(combos)


n = int(input())
s = list(input().split())
k = int(input())

prob = get_probability(s, k, 'a')
print('%.3f' % prob)

