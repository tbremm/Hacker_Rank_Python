import re


def solve(s):
    # Preserve whitespaces
    names = re.split(r'(\s+)', s)
    out = ""
    for name in names:
        out += name.capitalize()
    return out


s_in = input()
print(solve(s_in))

