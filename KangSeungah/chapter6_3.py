N = int(input())

array = []

for i in range(N):
    info = input().split()

    array.append((info[0], int(info[1])))


def setting(data):
    return data[1]


array = sorted(array, key=setting)

for name in array:
    print(name[0], end=' ')


