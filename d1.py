# 0 - 99
def secret_entrance():
    file = open('day1.txt')
    p = 0
    curr = 50
    for line in file:
        sign = line[0]
        val = int(line[1:])
        for i in range(val):
            if sign == 'L':
                curr = (curr - 1) % 100
            else:
                curr = (curr + 1) % 100
            if curr == 0:
                p += 1
    print(p)




