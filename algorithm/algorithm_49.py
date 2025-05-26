def solution(numbers):
    answer = []
    
    for idx,value in enumerate(numbers):
        now = value
        for i in range(idx+1,len(numbers)):
            if now+numbers[i] not in answer:
                answer.append(now+numbers[i])
                
    return sorted(answer)