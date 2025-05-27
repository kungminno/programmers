def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    correct = [0,0,0]
    
    for i,answer in enumerate(answers):
        if answer == first[i%5]:
            correct[0]+=1
        if answer == second[i%8]:
            correct[1]+=1
        if answer == third[i%10]:
            correct[2]+=1
            
    return sorted([i+1 for i,v in enumerate(correct) if v==max(correct)])