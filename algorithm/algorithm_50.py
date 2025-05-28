def solution(s):
    answer = []
    used = {}
    for i,v in enumerate(s):
        if v not in used:
            answer.append(-1)
        else:
            answer.append(i-used[v])
        used[v]=i    
    
    return answer