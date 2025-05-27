def divisors(num):
    div = []
    for i in range(1,int(num**0.5)+1):
        if num % i ==0:
            div.extend([i,num // i])
    return len(set(div))

def solution(number, limit, power):
    soldiers = []
    for i in range(1,number+1):
        if divisors(i) > limit:
            soldiers.append(power)
        else:
            soldiers.append(divisors(i))
    
    return sum(soldiers)