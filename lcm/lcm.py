# Uses python3
import sys

def u_gcd(a, b):

    if (a == 1 or b == 1):
        return 1

    for d in range(2, min(a, b) + 1):
        if (a > b):
            s = a % b
            if s == 0:
                return b
            else:
                a = s
        else:
            s = b % a
            if s == 0:
                return a
            else:
                b = s

def lcm(a, b):
    gcd = u_gcd(a, b)
    if (a > b):
        a = int(a / gcd)
    else:
        b = int(b / gcd)

    return a * b

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

