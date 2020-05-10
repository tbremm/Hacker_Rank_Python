# Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the
# average of all the plants with distinct heights in her greenhouse.
# Input Format
# The first line contains the integer, N, the total number of plants.
# The second line contains the N space separated heights of the plants.
#
# Constraints
# 0 < N <= 100
#
# Output Format
# Output the average height value on a single line.


def average(array):
    avg_set = set(array)
    return sum(avg_set) / len(avg_set)


plants = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174]
print(average(plants))