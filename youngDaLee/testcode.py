def solution(food_times, k):
    answer = k%len(food_times) # 모든 음식이 충분할 경우 돌아오는 위치
    cycle = k//len(food_times) # 회전 수

    print(answer, cycle)
    for i in range(len(food_times)):
        f = food_times[i]
        if f < cycle: # 회전 수 보다 음식 수가 적으면
            if i >= answer:
                answer += (cycle-f+1)
            else:
                answer += (cycle-f)
    
    answer = (answer%len(food_times)) +1
    return answer
print(solution([3, 1, 2], 5))