def solution(k, score):
    answer = []
    board = []
    for s in score:
        if len(board) < k:
            board.append(s)
        else:
            last = min(board)
            if last<s:
                board.remove(last)
                board.append(s) 
            
        answer.append(min(board))
    return answer

import heapq as hp

def solution(k, score):
    answer = []
    board = []
    for s in score:
        if len(board) < k:
            hp.heappush(board,s)
        else:
            if board[0]<s:
                hp.heappop(board)
                hp.heappush(board,s)
            
        answer.append(board[0])
    return answer