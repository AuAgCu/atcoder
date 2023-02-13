import itertools

N, W = map(int, input().split())
a = list(map(int, input().split()))

p1 = list(map(sum, itertools.permutations(a, 1)))
p2 = list(map(sum, itertools.permutations(a, 2)))
p3 = list(map(sum, itertools.permutations(a, 3)))

p1.extend(p2)
p1.extend(p3)
    
s = set(filter(lambda v: v <= W, p1))
print(len(s))
