def solution(a, b):
    week = {0:'FRI', 1:'SAT', 2:'SUN', 3:'MON', 4:'TUE', 5:'WED', 6:'THU'}
    month = {1:31, 2:29, 3:31 ,4:30, 5:31, 6:30, 7:31, 8:31, 9:30 ,10:31, 11:30}
    days = 0
    
    # 달이 바뀌면 일단 그 전달까지는 날이 지나감
    # 총 지나간 일수를 구하고 7로 나눈 나머지가 금요일부터 며칠이 지나갔는지를 알 수 있음
    # 이때 1일부터 시작하므로 지난달의 일수 + 현재 일수 -1
    for i in range(1,a):
        days += month[i]
    days += b - 1

    return week[days%7]
