from collections import Counter

EMPTY_COUNTER = Counter()


def MinWindowSubstring1(strArr):
    N, K = strArr
    frequencyK = Counter(K)
    options = []
    for i in range(len(N)):
        curr = Counter()
        for j in range(i, len(N)):
            curr[N[j]] += 1
            if frequencyK - curr == EMPTY_COUNTER:
                options.append(N[i:j + 1])
                break
    return min(options, key=len)
