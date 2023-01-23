import sys

s = input()

# 同じ文字が使われていないかのチェック
# setを使って重複文字を消して、その長さを比較することで、同じ文字が存在するかしないかをチェックしている。
if len(s) != len(set(s)):
    print("No")
    sys.exit()

# 大文字小文字が両方存在するかのチェック
# 全ての文字が大文字じゃないかチェック
if s.isupper():
    print("No")
    sys.exit()

# 全ての文字が小文字じゃないかチェック
if s.islower():
    print("No")
    sys.exit()

print("Yes")