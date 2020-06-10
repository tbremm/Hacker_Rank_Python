# https://www.hackerrank.com/challenges/itertools-product/problem

from itertools import product

A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))

# The '*' unpacks the list into tuples so it doesn't have the brackets when printing
print(*list(product(A, B)))
