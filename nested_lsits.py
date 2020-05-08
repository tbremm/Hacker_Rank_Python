# Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the
# name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a
# new line.
#
# Input Format
# The first line contains an integer, , the number of students.
# The  subsequent lines describe each student over  lines; the first line contains a student's name, and the second line
# contains their grade.
#
# Constraints
# There will always be one or more students having the second lowest grade.

# Output Format
# Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order
# their names alphabetically and print each one on a new line.


# Returns the second lowest in the input list
def find_second_worst(my_list):
    # dict.fromkeys removes duplicates, then we sort and take the second element
    return sorted(list(dict.fromkeys(my_list)))[1]


students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]
grades = []
for student in students:
    grades.append(student[1])

second_worst_grade = find_second_worst(grades)
second_worst_students = []

# Make sure to get and ties for second worst
for student in students:
    if student[1] == second_worst_grade:
        second_worst_students.append(student[0])

# Print out in alphabetical order, each on a new line
second_worst_students.sort()
print(*second_worst_students, sep="\n")
