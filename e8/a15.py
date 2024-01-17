N = int(input())
a = list(map(int, input().split()))

s = set(a)
arr = list(s)
arr.sort()

dic = {}
for i in range(len(arr)):
    dic[arr[i]] = i + 1

s = []
for v in a:
    s.append(str(dic[v]))

print(' '.join(s))