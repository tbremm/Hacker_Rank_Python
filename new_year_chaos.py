# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=arrays&isFullScreen=true&h_r=next-challenge&h_v=zen


def minimumBribes(q):
    num_bribes = 0
    for i, p in enumerate(q):
        if p - 1 - i > 2:
            print("Too chaotic")
            return
        for j in range(max(p - 2, 0), i):
            if q[j] > p - 1:
                num_bribes += 1
    print(num_bribes)
    return


good0 = [2, 1, 5, 3, 4]  # 3
too_chaotic0 = [2, 5, 1, 3, 4]
minimumBribes(good0)
minimumBribes(too_chaotic0)

good1 = [1, 2, 5, 3, 7, 8, 6, 4]  # 7
too_chaotic1 = [5, 1, 2, 3, 7, 8, 6, 4]
minimumBribes(good1)
minimumBribes(too_chaotic1)

good2 = [1, 2, 5, 3, 4, 7, 8, 6]  # 4
minimumBribes(good2)
