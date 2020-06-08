# https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


def arrayManipulation(n, queries):
    # Init list
    arr = [0] * (n + 1)

    # Update difference list, see link for explanation:
    # https://blogarithms.github.io/articles/2018-11/difference-arrays
    for a, b, k in queries:
        arr[a - 1] += k
        arr[b] -= k

    # Find max value
    count = 0
    temp = 0
    for i in arr:
        count += i
        if count > temp:
            temp = count

    return temp


    # The below is O(len(queries) * n)
    # arr = [0] * n
    # for op in queries:
    #     begin = op[0]
    #     end = op[1]
    #     add = op[2]
    #     for i, num in enumerate(arr[begin - 1:end]):
    #         arr[i + begin - 1] = num + add
    # return max(arr)


length = 10
# in_data = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
# in_data = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
in_data = [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]]
print(arrayManipulation(length, in_data))
