def solution(brown, yellow):
    width, height = 0, 0
#   둘레의 반
    half_length = brown//2 + 2
    size = brown + yellow
#   width >= height
#   가로,세로는 최소 3
    for i in range(3,half_length):
        if i*(half_length-i) == size:
            width = half_length-i
            height = i 
            return [width, height]
    