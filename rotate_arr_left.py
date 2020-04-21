# Rotate an array of length arr_length to the left "rotations" number of times
# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=arrays&isFullScreen=true


def rot_left(a, d):
    length = len(a)
    return a[d % length:] + (a[:d % length])


rotations = 10
arr_length = 8
arr = [i for i in range(arr_length)]
for r in range(rotations):
    print(rot_left(arr, r))