# 남은 콜라 개수가 a의 배수개면 전부, 아니라면 a의 배수개만큼만 주기
# 빈병 a개를 n//a묶음 가져가면, 콜라 b 병을 n//a묶음 준다
def solution(a, b, n):
    answer = 0
    while n >= a:
        give = a * (n//a)
        get = b*(n//a)
        n = n - give + get
        
        answer += get

    return answer