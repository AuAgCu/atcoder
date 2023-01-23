import sys

a, b = input().split()

# 大きい方をaにする
if a < b:
    a, b = b, a

# 桁が大きい方に合わせて０埋め、これで桁数が合って色々やりやすくなる
b = b.zfill(len(a))

for i in range(len(a)):
    if int(a[i]) + int(b[i]) >= 10:
        print('Hard')
        sys.exit(0)
    
print('Easy')