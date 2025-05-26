def solution(s, n):
    answer = ''
    caecar = 0

    for value in s:
        caecar = ord(value) + n
        # 대문자일때
        if value.isupper():
            if caecar > 90:
                caecar -= 26
        # 소문자일때
        elif value.islower():    
            if caecar > 122:
                caecar -= 26
        else:
            caecar = 32
        
        answer += chr(caecar)    
                
    return answer