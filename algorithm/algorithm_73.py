def moving(d, distance, position, block):
    directions = {'E':1,'W':-1,'S':1,'N':-1} # 동서남북
    r, c = position[0], position[1]
    if d in ['N','S']:
        r = r + directions[d] * int(distance)
        exists = any([i,c] in block for i in range(min(r,position[0]),max(r,position[0])+1))
    else: 
        c = position[1] + directions[d] * int(distance)
        exists = any([r,i] in block for i in range(min(c,position[1]),max(c,position[1])+1))
    
    return r,c,exists            
    
def solution(park, routes):
    block = []
    height = len(park)
    width = len(park[0])
    
    for r,row in enumerate(park):
        for c,col in enumerate(row):
            if col == 'S':
                position = [r,c]
            elif col == 'X':
                block.append([r,c])

    
    for route in routes:
        exists = False
        d, distance = route.split()
        r,c,exists = moving(d, distance, position, block)
        if (0 <= r < height) and (0 <= c < width) and not exists:     
            position = [r,c]        
            
    return position