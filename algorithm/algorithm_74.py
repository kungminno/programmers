def solution(id_list, report, k):
    user = {id:[i,0,[]] for i,id in enumerate(id_list)} # [0]idx,[1]신고당한 횟수,[2]본인을 신고한 사람
    answer = [0]*len(id_list)
    
    for r in report:
        do, reported = r.split()

        if do not in user[reported][2]:
            user[reported][2].append(do)
            user[reported][1] += 1

    for name,info in user.items():
        if info[1] >= k:
            for do in info[2]:
                answer[user[do][0]] += 1
                
    return answer