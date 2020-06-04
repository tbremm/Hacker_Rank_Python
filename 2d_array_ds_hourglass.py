# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays


def hourglassSum(arr):
    sums = []
    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr[i]) - 1):
            sums.append(arr[i - 1][j - 1] + arr[i - 1][j] + arr[i - 1][j+1] + arr[i][j] + arr[i + 1][j - 1] + arr[i + 1][j] + arr[i + 1][j + 1])
    return max(sums)


in_data = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]

print(hourglassSum(in_data))
