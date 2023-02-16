s = input()

dic = {}
dic_reverse = {}

# 普通のabc順
alphabet = ""
for i in range(97, 123):
    c = chr(i)
    alphabet += c

for i in range(len(s)):
    c = alphabet[i]
    c_r = s[i]
    dic[c_r] = c
    dic_reverse[c] = c_r

# 方針: 与えられた文字列を一旦変換し、いつものソート関数が使えるようにする
# 入力例1: 
# abcdefghijklmnopqrstuvwxyz

# bacdefghijklmnopqrstuvwxzy

# abx → bax
# bzz → ayy
# bzy → ayz
# caa → cbb

# 変換後のものを使ってソートする
# ayy
# ayz
# bax
# cbb

# 変換した名前を元に戻す。
# azz → bzz
# azy → bzy
# bax → abx
# caa → cbb

names = []
N = int(input())
for _ in range(N):
    name = input()
    coverted_name = ''.join(map(lambda x: dic[x], name))
    names.append(coverted_name)

names = sorted(names)
for name in names:
    reversed_name = ''.join(map(lambda x: dic_reverse[x], name))
    print(reversed_name)
