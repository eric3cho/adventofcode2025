import numpy as np


# 0 - 99
def secret_entrance():
    file = open('day1.txt')
    password = 0
    curr = 50
    prev = 0
    for line in file:
        sign = line[0]
        val = int(line[1:])
        if sign == 'R':
            curr += val
        else:
            curr -= val
        is_zero = (abs(curr) % 100 == 0) or (curr == 0)
        if is_zero and sign == 'L':
            password += 1
        dial = curr // 100
        if dial != prev:
            password += abs(dial-prev)
        prev = dial
    print(password)

