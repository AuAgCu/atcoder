N = int(input())

dic = {}
for _ in range(N):
    a, b = map(int, input().split())

    dic.setdefault(a, [])
    dic.setdefault(b, [])
    dic[a].append(b)
    dic[b].append(a)

stack = [1]
is_visit = set()
max_kaisu = 1
while len(stack):
    kaisu = stack.pop()
    if kaisu in is_visit:
        continue

    if kaisu > max_kaisu:
        max_kaisu = kaisu

    
    is_visit.add(kaisu)
    for next_kaisu in dic.get(kaisu, []):
        stack.append(next_kaisu)

print(max_kaisu)