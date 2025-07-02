def solution(progresses, speeds):
    answer = [1]
    complete_days = []
    previous_day = 0
    
    for i,v in enumerate(progresses):
        day ,left = divmod(100-v,speeds[i])
        if left != 0:
            day += 1
        complete_days.append(day)
        
    for i in range(1, len(complete_days)):
        # 우선순위가 먼저인 작업이 나보다 늦게 끝날때
        # 바로 앞 순서가 나보다 먼저 끝나도 그 앞 순서들이 늦게 끝날 때까지 고려 필요
        if complete_days[i]<=complete_days[i-1]:
            if previous_day == 0:
                previous_day = complete_days[i-1]
        
        if complete_days[i] <= previous_day:
            answer[-1] += 1
        else: 
            answer.append(1)
            previous_day = 0

    return answer