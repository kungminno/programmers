def solution(elements):
    answer = []
    array = elements*2
    # 몇개를 더할지
    for l in range(1,len(elements)+1):
        comb = sum(array[0:l])
        answer.append(comb)
        # 시작위치
        for i in range(1,len(elements)):
            comb = comb + array[i+l-1] - array[i-1]
            answer.append(comb)
    answer = set(answer)

    return len(answer)