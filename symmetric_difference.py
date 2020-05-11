# m = int(input())
# a = set(map(int, input().split()))
# n = int(input())
# b = set(map(int, input().split()))

a = {2, 4, 5, 9}
b = {2, 4, 11, 12}

sym_diff_a = list(a.difference(b))
sym_diff_b = list(b.difference(a))
sym_diff = sym_diff_a + sym_diff_b
sym_diff = sorted(sym_diff)

for i in range(len(sym_diff)):
    print(sym_diff[i])


