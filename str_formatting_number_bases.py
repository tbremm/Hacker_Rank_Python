# https://www.hackerrank.com/challenges/python-string-formatting/problem


def print_formatted(number):
    pad = len(str(bin(number).lstrip('0b').rstrip('L'))) + 1  # How big to pad the non-bin numbers
    for i in range(1, number + 1):
        print(str(i).rjust(pad - 1, ' ') + str(oct(i)).lstrip("0o").rstrip("L").rjust(pad, ' ') + str(hex(i).upper().lstrip("0X").rstrip("L").rjust(pad, ' ') + str(bin(i).lstrip("0b").rstrip("L").rjust(pad))))


test = 2
print_formatted(test)
