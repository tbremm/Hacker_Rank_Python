# Task
# You have a non-empty set s, and you have to execute N commands given in N lines.
# The commands will be pop, remove and discard.
#
# Input Format
# The first line contains integer n, the number of elements in the set s.
# The second line contains n space separated elements of set s. All of the elements are non-negative integers, less than
# or equal to 9.
# The third line contains integer N, the number of commands.
# The next N lines contains either pop, remove and/or discard commands followed by their associated value.
#
# Constraints
# 0 < n < 20
# 0 < N < 20
#
# Output Format
# Print the sum of the elements of set  on a single line.

num_in_s = 9
s = {1, 2, 3, 4, 5, 6, 7, 8, 9}
num_commands = 10
commands = ['pop', 'remove 9', 'discard 9', 'discard 8', 'remove 7', 'pop', 'discard 6', 'remove 5', 'pop', 'discard 5']

for command in commands:
    args = command.lower().split()
    if args[0] == 'remove':
        try:
            s.remove(int(args[1]))
        except KeyError:
            continue
    elif args[0] == 'discard':
        s.discard(int(args[1]))
    elif args[0] == 'pop':
        try:
            s.pop()
        except KeyError:
            continue

print(sum(s))




