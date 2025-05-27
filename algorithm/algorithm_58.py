from itertools import combinations

def prime_number(num):
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return True
    return False

def solution(nums):
    answer = 0
    
    for i in combinations(nums,3):
        if not prime_number(sum(i)):
            answer += 1

    return answer