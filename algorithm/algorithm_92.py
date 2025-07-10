from collections import deque
def solution(priorities, location):
    process = [(i,v) for i,v in enumerate(priorities)]
    process = deque(process)
    priorities.sort()
    max_v = priorities[-1]
    
    count = 0
    while True:
        turn, pri = process.popleft()

        if pri == max_v:
            count+=1
            if turn == location:
                return count
            priorities.pop()
            max_v = priorities[-1]
        else:
            process.append((turn, pri))