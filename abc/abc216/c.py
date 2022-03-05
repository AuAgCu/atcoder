n = int(input())

ans = ''
while n != 0:
    if n % 2 == 0:
        n //=2
        ans += 'B'
    else:
        n -=1
        ans += 'A'

print(''.join(reversed(ans)))  