def solution(sizes):
    long = 0
    short = 0
    for size in sizes:
        if max(size) > long:
            long = max(size)
        if min(size) > short:
            short = min(size)
    
    return long*short
        


# def solution(sizes):
#     # 가로 세로 중 길이가 긴 쪽을 long
#     # 가로 세로 중 길이가 짧은 쪽을 short
#     answer = 0
#     long = []
#     short = []
#     for size in sizes:
#         long.append(max(size))
#         short.append(min(size))
#     answer = max(long) * max(short)
#     return answer