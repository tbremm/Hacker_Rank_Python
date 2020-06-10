# https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem


def calc(a, b, c, d):
    return pow(a, b) + pow(c, d)


a_in = int(input())
b_in = int(input())
c_in = int(input())
d_in = int(input())

print(calc(a_in, b_in, c_in, d_in))
