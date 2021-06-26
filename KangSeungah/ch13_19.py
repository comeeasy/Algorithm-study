from itertools import permutations
# 중복순열

# 계산할 피연산자 개수
n = int(input())

# 피연산자
num = list(map(int, input().split()))

# 연산자 갯수
# if
# i == 0 : +, i == 1 : -, i == 2 : *, i == 3 : //
op = list(map(int, input().split()))

# 존재하는 연산자를 다시 new_op에 정리
new_op = []
for i in range(4):
    if i == 0:
        if op[i] != 0:
            for j in range(op[i]):
                new_op.append('+')
    elif i == 1:
        if op[i] != 0:
            for j in range(op[i]):
                new_op.append('-')
    elif i == 2:
        if op[i] != 0:
            for j in range(op[i]):
                new_op.append('*')
    else:
        if op[i] != 0:
            for j in range(op[i]):
                new_op.append('//')


def factorial(x):
    n = 1
    for i in range(1, x+1):
        n = n*i
    return n


cases = permutations(new_op,n-1)

for i in range(4):
    if op[i] > 1:
        cases /= factorial(op[i])


# final
# sum += 연속적으로 답을 저장

