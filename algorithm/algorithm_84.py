def solution(s):
    answer = 0
    dic = {')':'(', '}':'{', ']':'['}

    for i in range(len(s)):
        array = [ ]# 소/중/대괄호
        count = 0
        for j in range(len(s)):
            idx = (i+j)%len(s)
            # 여는 괄호면 push
            if s[idx] in ['(', '{', '[']:
                array.append(s[idx])
            # 닫는 괄호면 pop, 근데 stack이 비어있다? -> 성립 X
            else:
                if array:
                    # 늦게 나온 괄호가 먼저 닫혀야 함
                    # 닫는 괄호가 가장 늦게 들어간 여는 괄호가 아니다? -> 성립 X
                    if array.pop() != dic[s[idx]]:
                        break
                    count += 1
                else:
                    break

            if count == len(s)/2:
                answer += 1

    return answer