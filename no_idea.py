# nm = list(map(int, input().split()))
# in_list = list(map(int, input().split()))
# a = set(map(int, input().split()))
# b = set(map(int, input().split()))

n = 3
m = 2
in_list = [1, 5, 3, 3]
a = {3, 1}
b = {5, 7}
happiness = 0  # Should end at 2

# Must optimize, times out in HR
for num in in_list:
    if num in a:
        happiness += 1
    elif num in b:
        happiness -= 1
print(happiness)
