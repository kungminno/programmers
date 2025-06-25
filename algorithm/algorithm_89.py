def solution(want, number, discount):
    answer = 0
    want_list = {v:num for v,num in zip(want, number)}
    for i in range(len(discount)):
        array = want_list.copy()
        for j in range(10):
            if i + j == len(discount):
                break
            product = discount[i+j]
            if product in want_list and array[product]>0:
                array[product] -= 1
            
            if sum(array.values()) == 0:
                answer+=1
    return answer