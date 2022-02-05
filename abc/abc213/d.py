import sys
sys.setrecursionlimit(2 * 10**6)

def recurtion(root, v, flags):
    flags[v] = True
    print(v+1, end=" ")
    if v not in root.keys():
        return
    
    for w in root[v]:
        if flags[w]:
            continue
        
        recurtion(root, w, flags)
        print(v+1, end=" ")

n = int(input())

root = {}
for i in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    root.setdefault(a, [])
    root.setdefault(b, [])

    root[a].append(b)
    root[b].append(a)

for k, v in root.items():
    v.sort()

recurtion(root, 0, [False] * n)


