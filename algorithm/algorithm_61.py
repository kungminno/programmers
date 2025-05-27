# min -> 모르는 번호 2개가 다 틀린경우
# max -> 모르는 번호 2개가 다 맞은경우

def solution(lottos, win_nums):
    ranking = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    same, zero = 0, 0
    lottos.sort()
    win_nums.sort()
    
    for i in lottos:
        if i in win_nums:
            same +=1
        elif i == 0:
            zero += 1
            
    return [ranking[same+zero],ranking[same]]