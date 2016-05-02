# Uses python3
import sys

# def gcd(a, b):
#     current_gcd = 1
#     for d in range(2, min(a, b) + 1):
#         if a % d == 0 and b % d == 0:
#             if d > current_gcd:
#                 current_gcd = d
#
#     return current_gcd

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

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    # print(gcd(a, b))
    print(u_gcd(a, b))
