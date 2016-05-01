# Uses python3
import sys

def get_fibonacci_last_digit(n):
    if (n <= 1):
        return n

    prev_num = 1
    prev_prev_num = 0

    for i in range(2, n):
        temp_pp_num = prev_prev_num
        prev_prev_num = prev_num
        prev_num = prev_num + temp_pp_num
        if prev_num > 9:
            prev_num = prev_num % 10

        if prev_prev_num > 9:
            prev_prev_num = prev_prev_num % 10

    if (prev_num + prev_prev_num) > 9:
        return (prev_num + prev_prev_num) % 10
    else:
        return prev_num + prev_prev_num

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
