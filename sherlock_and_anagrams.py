# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps&h_r=next-challenge&h_v=zen

from collections import Counter

def sherlockAndAnagrams(s):
    # From the discussion section - requires further study
    count = 0
    for i in range(1, len(s) + 1):
        a = ["".join(sorted(s[j:j + i])) for j in range(len(s) - i + 1)]
        b = Counter(a)
        for j in b:
            count += b[j] * (b[j] - 1) / 2
    return int(count)


test = ['ifailuhkqq', 'kkkk']

for s in test:
    print(sherlockAndAnagrams(s))
