import sys

list_a = []
n = int(sys.stdin.readline())

for i in range(n):
    str = sys.stdin.readline().split()
    if str[0] == 'push':
        list_a.append(str[1])
    elif str[0] == 'top':
        if len(list_a) == 0:
            print(-1)
        else:
            print(list_a[-1])
    elif str[0] == 'size':
        print(len(list_a))
    elif str[0] == 'pop':
        if len(list_a) == 0:
            print(-1)
        else:
            print(list_a.pop())
    elif str[0] == 'empty':
        if len(list_a) == 0:
            print(1)
        else:
            print(0)
