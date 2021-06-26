s = input()

# 최대값
result = int(s[0])

for i in range(1, len(s)):
    # 0과 1의 경우
    if result == 0 or result == 1 or int(s[i]) == 0 or int(s[i]) == 1:
        result += int(s[i])
    # 0과 1이 아닌 경우
    else:
        result *= int(s[i])

print(result)


