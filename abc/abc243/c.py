import sys
N = int(input())

positions = []
for _ in range(N):
    x, y = map(int, input().split())
    positions.append((x, y))

s = input()

dic = {}
for i in range(N):
    x, y = positions[i]
    direction = s[i]
    dic.setdefault(y, [])
    dic[y].append((x, direction))

for arr in dic.values():
    arr = sorted(arr)
    exist_right = False
    for _, direction in arr:
        if direction == 'L' and exist_right:
            print('Yes')
            sys.exit()

        if direction == 'R':
            exist_right = True

print('No')

# TODO: 今度出す