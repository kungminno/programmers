def solution(cards1, cards2, goal):

    while True:
        if cards1[0:1] == [goal[0]]:
            goal.pop(0)
            cards1.pop(0)
        elif cards2[0:1] == [goal[0]]:
            goal.pop(0)
            cards2.pop(0)
        else:
            return "No"
        
        if len(goal) == 0:
            return "Yes"