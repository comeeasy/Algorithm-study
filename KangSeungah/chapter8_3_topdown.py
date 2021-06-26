n = int(input())

k = list(map(int, input().split()))

maximum = [0] * 100

maximum[0] = k[0]
maximum[1] = max(maximum[0], k[1])


def topdown(i):
    if i == 0:
        return maximum[0]
    if i == 1:
        return maximum[1]

    maximum[i] = max(topdown(i-1), k[i] + topdown(i-2))

    return maximum[i]


topdown(n-1)

