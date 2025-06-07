def substring(a, b):
    from collections import Counter

    count_a = Counter(a)
    count_b = Counter(b)

    result = []
    for ch in sorted(set(a + b)):
        common = min(count_a[ch], count_b[ch])
        result.extend([ch] * common)

    return ''.join(result)

a = input()
b = input()
print(substring(a, b))
