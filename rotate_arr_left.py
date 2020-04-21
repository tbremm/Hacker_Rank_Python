# Rotate an array of length arr_length to the left "rotations" number of times


def rot_left(a, d):
    length = len(a)
    return a[d % length:length] + (a[:d % len(a)])


rotations = 5
arr_length = 8
arr = [i for i in range(arr_length)]
for r in range(rotations):
    print(rot_left(arr, r))