def solution(n):
    answer = ''
    word = ['수','박']
    
    for i in range(n):
        answer+=word[i%2]
    
    return answer