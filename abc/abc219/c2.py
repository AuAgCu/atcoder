from functools import cmp_to_key

s = input()
N = int(input())
names = []
for i in range(N):
    names.append(input())


def compare(a, b):
    for i in range(min(len(a), len(b))):
        sa = a[i]
        sb = b[i]

        if sa == sb:
            continue

        findIndexA = s.find(sa)
        findIndexB = s.find(sb)
        return findIndexA - findIndexB

    return len(a) - len(b)
    
names = sorted(names, key=cmp_to_key(compare))

for name in names:
    print(name)
