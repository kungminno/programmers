def solution(s):
    count = [0,0]

    while s != '1':
        temp = ''
        for v in s:
            if v == '0':
                count[1] += 1
            else:
                temp += v

        s = bin(len(temp))[2:]
        count[0] += 1
                
    return count