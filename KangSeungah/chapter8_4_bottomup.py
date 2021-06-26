n = int(input())

case = [0] * 1000

case[1] = 1
case[2] = 3

for i in range(3, n+1):
    case[i] = (case[i-1] + case[i-2] * 2) % 796796

print(case(n))

