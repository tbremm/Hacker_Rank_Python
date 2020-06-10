# https://www.hackerrank.com/challenges/alphabet-rangoli/problem?h_r=next-challenge&h_v=zen


def print_rangoli(size):
    width = (size * 4) - 3
    charr = [''] * size
    for row in range(size):
        for c in range(row + 1):
            charr[row] += chr(size - c + 96)
        if row != 0:
            charr[row] += charr[row][-2::-1]
    for i in charr:
        print('-'.join(i).center(width, '-'))
    for i in reversed(charr):
        if i == charr[len(charr) - 1]:
            continue
        print('-'.join(i).center(width, '-'))


test = 5
print_rangoli(test)
