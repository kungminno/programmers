def solution(s, skip, index):
    answer = ''
    
    for word in s:
        trans = ord(word)
        i = 0
        while i < index:
            i+=1
            trans += 1
            if trans > 122:
                trans = 97
            if chr(trans) in skip:
                i -= 1
        answer += chr(trans)
    return answer