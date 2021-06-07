# 문자열 u,v로 자르는 함수
def split_li(li):
    left = 0
    right = 0
    c = 0
    for i in range(len(li)):
        if li[i] =='(':
            left += 1
        elif li[i] ==')':
            right+=1
        if left==right:
            c = i
            break
    u, v = li[:c+1], li[c+1:] 

    return (u, v)

# 문자열 올바른지 판별하는 함수
def is_right(li):
    stack = []
    idx = 0
    while idx<len(li):
        top = li[idx]
        if not stack:
            stack.append(top)
        elif stack[-1] == '(' and top==')':
            stack.pop(-1)
        else:
            stack.append(top)
        idx += 1
    if stack: # stack에 뭔가 남아있으면 False
        return False
    else: # stack에 남은거 없으면 True
        return True

# 4-4 수행
def convert(li):
    # u의 첫번째와 마지막 문자 제거
    li.pop(0)
    li.pop(-1)

    if not li: # 빈 리스트면
        return []
    # 나머지 문자열 괄호 방향 뒤집어서 뒤에 붙임
    else:
        for i in range(len(li)):
            if li[i]=='(':
                li[i]=')'
            else:
                li[i]='('
        return li

# 4-1~4-5 수행
def change_li(p):
    answer = ''
    if len(p) == 0:
        return []
    
    u, v = split_li(p)

    if is_right(u):
        return u + change_li(v)
    else:
        new_u = convert(u)
        return ['(']+change_li(v)+[')']+new_u

def solution(p):
    p = list(p)
    answer = change_li(p)
    return ''.join(answer)
    

p = "(()())()"
print(solution(p))