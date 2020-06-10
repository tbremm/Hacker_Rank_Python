# https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem


def calc(a, b, c, d):
    return pow(a, b) + pow(c, d)


a_in, b_in, c_in, d_in = (int(input()) for _ in range(4))

print(calc(a_in, b_in, c_in, d_in))
