def solution(citations):
    citations.sort()
    for i,v in enumerate(citations):
        c_num = v
        paper_num = len(citations) - i
        # print(f'{c_num}번 이상 인용된 논문이 {paper_num}편')
        if c_num >= paper_num:
            return paper_num

    return 0