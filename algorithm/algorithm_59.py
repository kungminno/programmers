def solution(n, m, section):
    answer = 1
    left = section.copy()
    paint = section[0]+m-1
    
    for s in section:
        if s in left:
            if s <= paint:
                left.remove(s)
            else:
                paint = s+m-1
                answer+=1
                
    return answer

# 간단한 버전
def solution(n, m, section):
    answer = 1
    paint = section[0]+m-1
    
    for s in section:
        if s <= paint:
            continue
        else:
            paint = s+m-1
            answer+=1
                
    return answer

# 더 간단한 버전
def solution(n, m, section):
    answer = 1
    paint = section[0]+m-1
    
    for s in section:
        if s > paint:
            paint = s+m-1
            answer+=1
                
    return answer