import sys
H, W = map(int, input().split())
s = []

s.append('#' * (W+4))
s.append('#' * (W+4))
for _ in range(H):
    s.append('##' + input() + '##')
s.append('#' * (W+4))
s.append('#' * (W+4))

a = [[100 for _ in range(W+4)] for _ in range(H+4)]
a[2][2] = 0
for i in range(2, H+2):
    for j in range(2, W+2):
        if s[i][j] == '.':
            a[i][j] = min(a[i-1][j], a[i+1][j], a[i][j-1], a[i][j+1], a[i][j])
        else:
            a[i][j] = min(a[i][j], min(min(a[i-2][j-1:j+2]), min(a[i-1][j-2:j+3]), min(a[i][j-2:j+3]), min(a[i+1][j-2:j+3]), min(a[i+2][j-1:j+2])) + 1)

print(a[-3][-3])



for v in a:
    print(*v)
for v in s:
    print(*v)