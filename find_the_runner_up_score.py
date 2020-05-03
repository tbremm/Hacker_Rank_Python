def find_runner_up(arr):
    s_arr = sorted(arr, reverse=True)
    for i in range(len(s_arr)):
        if i == len(s_arr):
            return s_arr[i]
        elif s_arr[i + 1] < s_arr[i]:
            return s_arr[i + 1]
    return -1  # Error


a = [6, 10, 2, 4, 3, 5, 8]
print(find_runner_up(a))