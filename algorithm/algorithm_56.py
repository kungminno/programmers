# 가능한 높은 점수부터 담자
def solution(k, m, score):
    if len(score) < m:
        return 0
    
    answer = 0
    score.sort(reverse=True)
    
    for i in range(0,len(score),m):
        if i+m <= len(score):
            answer += score[i:i+m][-1]*m
    
    return answer