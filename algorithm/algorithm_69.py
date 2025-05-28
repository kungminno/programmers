def solution(survey, choices):
    answer = ''
    choice_scores = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}
    personality_counts = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}

    for i,value in enumerate(survey):
        if choices[i] > 4:
            personality_counts[value[1]] += choice_scores[choices[i]]
        else:
            personality_counts[value[0]] += choice_scores[choices[i]]
        
    for i,type in enumerate(personality_counts):
        if i % 2 == 0:
            previous_type = type
            previous_value = personality_counts[type]
        else:
            if previous_value >= personality_counts[type]:
                answer += previous_type
            else:
                answer += type
        
    return answer