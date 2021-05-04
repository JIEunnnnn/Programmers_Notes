

#1차시도 -> 정확성 12.5
from copy import deepcopy 
from collections import deque 

def sumwith(N, K, maps, x, y, val, cnt) :
    maps = deepcopy(maps) 
    
    if maps[x][y] != 0 :
        val += maps[x][y]
        if val <= K : #걸리는시간이 K보다는 작아야함
            cnt += 1 
        else :
            return cnt
    
    for will_y, will_values in enumerate(maps[y]) :
        if will_values != 0 :
            cnt = sumwith(N, K, maps, y, will_y, val, cnt)

    return cnt     
    
    
    

def solution(N, road, K):
    answer = 1
    
    maps = [[0 for i in range(N)] for j in range(N)]
    willdo = deque()
    for x,y,z in road :
        if x > y :
            x,y = y, x 
        
        maps[x-1][y-1] = z 
        if x-1 == 0 :
            willdo.append(y-1)
            
    values = 0 
    for w in willdo :
        answer += sumwith(N,K,maps,0, w, values, 0)
        
    return answer
