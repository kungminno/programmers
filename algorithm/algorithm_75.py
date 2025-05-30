def solution(s):
    num = list(map(int,s.split(' ')))
    
    return ' '.join([f'{min(num)}',f'{max(num)}'])