# 가장 큰 수 기준으로 가야됨
def solution(arr):
    i = 0
    big = max(arr)
    while 1:
        i += 1
        n = big * i
        if sum([n%i for i in arr]) == 0:
            return n