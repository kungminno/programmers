# 순서가 1,2,3,1인 경우만 가능
def solution(ingredient):
    answer = 0
    stack = []
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == [1,2,3,1]:
            del stack[-4:]
            answer+=1

    return answer