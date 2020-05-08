student_marks = {'Krishna': [67.0, 68.0, 69.0], 'Arjun': [70.0, 98.0, 63.0], 'Malika': [52.0, 56.0, 60.0]}
query_name = 'Malika'


def find_avg_marks(marks, name):
    m = marks[name]
    return sum(m) / len(m)


print('%.2f' % find_avg_marks(student_marks, query_name))
