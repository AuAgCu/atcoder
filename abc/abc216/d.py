import heapq

def minus(s):
    return int(s) - 1
    
N, M = map(int, input().split())
qs = []
for _ in range(M):
    _ = input()
    q = list(reversed(list(map(minus, input().split()))))
    qs.append(q)

queue = []
dic = {i: [] for i in range(N)}
for i in range(M):
    color = qs[i].pop()
    dic[color].append(i)
    if len(dic[color]) == 2:
        queue.append(color)

count = 0
while len(queue):
    color = queue.pop()
    arr = dic.pop(color)
    for v in arr:
        if len(qs[v]):
            color = qs[v].pop()
            dic[color].append(v)
            if len(dic[color]) == 2:
                queue.append(color)
    
    count += 2

if count == N * 2:
    print('Yes')
else:
    print('No')