def solution(X, Y):
    # 배열의 각 숫자의 개수
    array_x = [0]*10
    array_y = [0]*10
    common = []
    
    for x in X:
        array_x[int(x)]+=1
    for y in Y:
        array_y[int(y)]+=1
    
    for i in range(9,-1,-1):
        # i -> 숫자, array_y[i],array_x[i] -> 개수
        if array_x[i] == 0 and array_y[i] == 0:
            continue
        elif array_x[i] >= array_y[i]:
            common.extend(str(i) * array_y[i])
        elif array_x[i] < array_y[i]:
            common.extend(str(i) * array_x[i])
    
    result = ''.join(common)
    if not result:
        return "-1"
    elif result[0] == "0":
        return "0"
    else:
        return result