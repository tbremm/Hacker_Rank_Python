#  https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&h_r=next-challenge&h_v=zen&isFullScreen=true&playlist_slugs%5B%5D%5B%5D%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D%5B%5D%5B%5D=arrays&h_r=next-challenge&h_v=zen


def minimumSwaps(arr):
    swaps = 0
    arr = [x - 1 for x in arr]                  # Subtract one from each arr[x] so it matches the index
    val_dict = {x:i for i, x in enumerate(arr)} # Create lookup dict of sorted -> not sorted
    for i, x in enumerate(arr):                 # Enum arr so we can compare i and x
        if i != x:                              # This x doesn't belong at this index, so swap it out
                                                # Send x where it belongs (associated with it's matching index)





        # min_of_arr = min(arr[i + 1:])
        # if arr[i] > min_of_arr:
        #     min_index = arr[i + 1:].index(min_of_arr)  # Get the index of the smallest remaining value
        #     temp = arr[i]
        #     arr[i] = arr[min_index]
        #     arr[min_index] = temp
        #     swaps += 1
            return swaps


test_arr = [7, 1, 3, 2, 4, 5, 6]
# print(minimumSwaps(test_arr))


def other_minimum_swaps(arr):
    res = 0
    arr = [x-1 for x in arr]
    value_idx = {x:i for i, x in enumerate(arr)}
    for i, x in enumerate(arr):
        if i != x:
            to_swap_idx = value_idx[i]
            value_idx[i] = i
            value_idx[x] = to_swap_idx
            arr[i], arr[to_swap_idx] = i, x
            res += 1
    print(res)
    return res


print(other_minimum_swaps(test_arr))
