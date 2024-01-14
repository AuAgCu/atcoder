import bisect

N, X = map(int, input().split())
a = list(map(int, input().split()))

print(bisect.bisect_left(a, X) + 1)