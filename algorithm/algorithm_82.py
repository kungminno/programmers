# 즉 피보나치 수열
def solution(n):
    if n == 1:
        return 1
    
    a,b = 1,2
    for i in range(1,n-1):
        a, b = b, a+b

    return b%1234567