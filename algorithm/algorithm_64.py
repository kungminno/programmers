def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    lost_copy = lost.copy()
    
    for l in lost:
        if l in reserve:
            lost_copy.remove(l)
            reserve.remove(l)
    
    lost = lost_copy[:]
    for l in lost:
        if l-1 in reserve:
            lost_copy.remove(l)
            reserve.remove(l-1)
        elif l+1 in reserve:
            lost_copy.remove(l)
            reserve.remove(l+1)
    
    return n-len(lost_copy)

def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    reserve_copy = reserve.copy()
    
    for r in reserve:
        if r in lost:
            lost.remove(r)
            reserve_copy.remove(r)
    
    for r in reserve_copy:
        if r-1 in lost:
            lost.remove(r-1)
        elif r+1 in lost:
            lost.remove(r+1)
    
    return n-len(lost)