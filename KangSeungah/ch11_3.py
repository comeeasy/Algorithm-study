s = input()
count_0 = 0
count_1 = 0

if int(s[0]) == 0:
    count_0 = 1
elif int(s[0]) == 1:
    count_1 = 1

# 다음 원소를 기준으로 바뀌는 지점을 count += 1 실행
for i in range(len(s)-1):
    if int(s[i]) == 0:
        if int(s[i+1]) == 1:
            count_1 += 1

    elif int(s[i]) == 1:
        if int(s[i+1]) == 0:
            count_0 += 1

print(min(count_1, count_0))


