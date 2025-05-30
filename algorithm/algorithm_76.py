def solution(s):
    answer = ''
    first = True
    
    for word in s:
        if word != ' ':
            if first:
                answer += word.upper()
            else:
                answer += word.lower()
            first = False
        else:
            answer += word
            first = True
            
    return answer