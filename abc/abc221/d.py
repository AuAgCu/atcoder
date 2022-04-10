N = int(input())
a = []
b = []

dic = {}
for _ in range(N):
    c, d = map(int,input().split())
    dic.setdefault(c, 0)
    dic.setdefault(c+d, 0)
    a.append(c)
    b.append(d)

    dic[c] += 1
    dic[c+d] -= 1

last = 0
count = 0
array = [0 for i in range(N+1)]
for k in sorted(dic.keys()):
    array[count] += k - last
    count += dic[k]

    last = k

for v in array[1:]:
    print(v, end=" ")