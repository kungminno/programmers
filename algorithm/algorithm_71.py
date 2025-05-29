# 유효기간 날짜가 더 작으면 파기
def solution(today, terms, privacies):
    answer = []
    kinds = {}
    
    for term in terms:
        t, month = term.split()
        kinds[t]=int(month)
    
    for i,privacy in enumerate(privacies):
        date, k = privacy.split(' ')
        y, m, d = date.split('.')
        m = int(m) + kinds[k]%12
        y = int(y)  + kinds[k]//12
        if m > 12:
            y  += 1
            m -= 12

        if today>= '.'.join([f"{y}",f"{m:02d}",d]):
             answer.append(i+1)      
    
    return answer