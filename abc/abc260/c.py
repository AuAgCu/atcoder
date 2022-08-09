def convert(X, Y, n, red, blue):
    if n == 1:
        return red, blue
    
    blue += red * X

    next_red = blue + red
    next_blue = blue * Y

    return convert(X, Y, n - 1, next_red, next_blue)

N, X, Y = map(int, input().split())

red, blue = convert(X, Y, N, 1, 0)
print(blue)
