# https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays&h_r=next-challenge&h_v=zen

def minimumSwaps(arr):
    res = 0
    arr = [x - 1 for x in arr]
    value_idx = {x: i for i, x in enumerate(arr)}
    for i, x in enumerate(arr):
        if i != x:
            to_swap_idx = value_idx[i]
            value_idx[i] = i
            value_idx[x] = to_swap_idx
            arr[i], arr[to_swap_idx] = i, x
            res += 1
    return res


in_data = [7, 1, 3, 2, 4, 5, 6]
print(minimumSwaps(in_data))
