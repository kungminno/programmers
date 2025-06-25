#  옷을 안 걸친다 까지 포함해서 각 의상 별 가능한 경우의 수는 len(의상종류)+1
#  이때 한 벌이라도 입고있어야하니 결과는 -1
def solution(clothes):
    answer = 1
    kinds = {}
    for cloth in clothes:
        if cloth[1] not in kinds:
            kinds[cloth[1]] = []
        kinds[cloth[1]].append(cloth[0])
    
    for _,item in kinds.items():
        answer *= len(item)+1
    
    return answer-1