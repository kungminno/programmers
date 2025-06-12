from collections import Counter

def solution(k, tangerine):
    if len(tangerine) <= k:
        return len(set(tangerine))
    
    kinds,nums = 0, 0
    tangerine_nums = sorted(Counter(tangerine).values(),reverse=True)
    while nums < k:
        nums += tangerine_nums[kinds]
        kinds += 1
    
    return kinds