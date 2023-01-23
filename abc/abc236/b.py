input()
arr = list(map(int, input().split()))

dic = {}
for num in arr:
    dic.setdefault(num, 0)
    dic[num] += 1

for k, v in dic.items():
    if v == 3:
        print(k)
        exit(0)