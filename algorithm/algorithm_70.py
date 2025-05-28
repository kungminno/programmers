import heapq as hp
def solution(wallpaper):
    row = [[52],[0]]
    column = [[52],[0]]
    
    for r,value in enumerate(wallpaper):
        for c,v in enumerate(value):
            if v == '#':  
                hp.heappush(row[0],r)
                hp.heappush(row[1],-r)
                hp.heappush(column[0],c)
                hp.heappush(column[1],-c)


    return [row[0][0],column[0][0], -row[1][0]+1,-column[1][0]+1]