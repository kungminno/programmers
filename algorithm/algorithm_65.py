def solution(s):
    answer, i = 0, 0
    now = s[0]
    equal, diff = 0, 0
    
    while i < len(s):
        compare = s[i]
        if compare == now:
            equal += 1
        else:
            diff += 1
        
        # 마지막에 다다르면 equal == diff이면 +1, equal != diff 이어도 문자열을 분해하기에 +1
        # 따라서 마지막에 다다르면 어찌 되어도 +1
        if i == len(s)-1:
                answer += 1
        else:
            if equal == diff:
                answer += 1
                now = s[i+1]
                equal, diff = 0, 0
        i+=1
            
    return answer