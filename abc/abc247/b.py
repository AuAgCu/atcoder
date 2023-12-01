n = int(input())

names = []
dic = {}
for i in range(n):
    first, last = input().split()
    names.append((first, last))

    dic.setdefault(first, 0)
    dic.setdefault(last, 0)

    dic[first] += 1
    dic[last] += 1

    if first != last:
        dic[last] += 1

for v in names:
    if dic[v[0]] > 1 and dic[v[1]] > 1:
        print("No")
        exit()

print("Yes")