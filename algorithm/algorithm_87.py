# r,c 비교했을 때 큰 쪽이 해당됨
def solution(n, left, right):
    answer = []
    first = left//n
    for r in range(first,n):
        for c in range(n):
            value = max(r+1,c+1)
            idx = r*n + c 
            if left <= idx <=right:
                answer.append(value)  
            elif idx > right:
                break
    return answer