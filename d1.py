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

def git_shop():
    file = open('day2.txt')
    sum = 0
    id = []
    for line in file:
        id = line.strip().split(",")
    for x in id:
        ranges = x.split("-")
        a = int(ranges[0])
        b = int(ranges[1])
        for i in range(a, b+1):
            i_str = str(i)
            if len(i_str) % 2 == 0:
                mid = int(len(i_str) / 2)
                if i_str[0:mid] == i_str[mid:]:
                    sum += i
    print(sum)
