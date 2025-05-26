def solution(s):
    answer = ''
    words = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    number =''
    
    for i in s:
        try:
            answer+= str(int(i))
        except ValueError:
            number+=i
            if number in words.keys():
                answer+= str(words[number])
                number = ''

    return int(answer)