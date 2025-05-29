def solution(players, callings):
    player_based_rank = {player:i for i,player in enumerate(players)}
    number_based_rank = {i:player for i,player in enumerate(players)}

    for player in callings:
        # 원래 등수
        my = player_based_rank[player]
        # 바뀐 등수(숫자)
        change = my - 1
        # 내가 앞지른 사람
        front = number_based_rank[change]
        
        # 본인 정보 교체
        player_based_rank[player] = change
        number_based_rank[change] = player
        # 원래 등수 사람 정보 교체
        player_based_rank[front] = my
        number_based_rank[my] = front
        
    return list(number_based_rank.values())