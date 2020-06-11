# https://www.hackerrank.com/challenges/compress-the-string/problem

from itertools import groupby

in_str = input()
groups = []
ukeys = []

for k, g in groupby(in_str):
    groups.append(list(g))
    ukeys.append(k)

out_str = ''
for i, key in enumerate(ukeys):
    out_str += '(' + str(len(groups[i])) + ', ' + key + ')'
    if i != len(ukeys) - 1:
        out_str += ' '
print(out_str)
