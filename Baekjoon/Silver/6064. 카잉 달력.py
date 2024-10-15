import sys

input = sys.stdin.readline


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
        print(f'a: {a}, b: {b}')
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


t = int(input())

for _ in range(t):
    M, N, x, y = map(int, input().split())

    l = lcm(M, N)
    print(f'l : {l}')
    found = False

    while x <= l:
        if (x - 1) % N + 1 == y:
            sys.stdout.write(str(x))
            found = True
            break
        x += M
        print(f'x: {x}')
    if not found:
        sys.stdout.write(str(-1))
