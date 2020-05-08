# Returns the second lowest in the input list
def find_second_worst(my_list):
    my_list.sort()  # Put lowest first, highest last
    for i in range(len(my_list)):
        if i == len(my_list):
            return my_list[i]
        elif my_list[i + 1] > my_list[i]:
            return my_list[i + 1]
    return -1  # error


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

# Print out in alphabetical order
second_worst_students.sort()
for second_worst in second_worst_students:
    print(second_worst)