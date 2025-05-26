def solution(s):
    answer = ''
    i = 0
# 공백이 연속으로 있는 경우 고려 필요
    for v in s:
        if v == ' ':
            i = 0
            answer += ' '
        else:
            if i%2 != 0:
                answer += v.lower()
            else:
                answer += v.upper()
            i+=1
    
    return answer