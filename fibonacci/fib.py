# Uses python3
from time import sleep, perf_counter as pc

t0 = pc()



def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


dic = {'key': 0}


def calc_fib_more_faster(n):
    if (n <= 1):
        return n

    if (n - 1) in dic:
        a = dic[n - 1]
    else:
        dic[n - 1] = calc_fib_more_faster(n - 1)
        a = dic[n - 1]

    if (n - 2) in dic:
        b = dic[n - 2]
    else:
        dic[n - 2] = calc_fib_more_faster(n - 2)
        b = dic[n - 2]

    return a + b

n = int(input())
# t0 = pc()
# print(calc_fib(n))
# print(pc()-t0)

t0 = pc()
print(calc_fib_more_faster(n))
print(pc()-t0)

