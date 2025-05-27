# 동일한게 두번 이상 반복되면 어차피 불가능
def solution(babbling):
    answer = 0
    says = ["aya", "ye", "woo", "ma"]

    for word in babbling:
        used = [True, True, True, True]
        match, final = "", ""
        for w in word:
            match += w
            if match in says and used[says.index(match)]:
                final += match
                used = [True, True, True, True]
                used[says.index(match)] = False
                match = ""
        
        if word == final:
            answer += 1                
                
    return answer

def solution(babbling):
    answer = 0  
    
    for b in babbling:
        word,final = "", ""
        if "ayaaya" in b or "yeye" in b or "woowoo" in b or "mama" in b:
            continue
        else:
            for w in b:
                word += w
                if word in ["aya", "ye", "woo", "ma"]:
                    final += word
                    word = ""
        
            if final == b:
                answer += 1       
                
    return answer

