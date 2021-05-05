





===========================================================
#2차시도 
from copy import deepcopy
from collections import deque 

def willchk(maps, visited, x, y , k) :
    #x,y 좌표 및 k라는 주어진 시간
    maps = deepcopy(maps)
    visited = deepcopy(visited) 
    cnt = 0
    que = deque([(x,y,0)])
    #print("xxxxxxxxx")
    while que :
        #print(que)
        #print(visited)
        #print(cnt)
        tx, ty, tz = que.popleft()
        if tx > ty :
            tx, ty = ty, tx
        
        if maps[tx][ty] != 0 :
            if visited[ty] == 0 and maps[tx][ty] + tz <= k:
                cnt +=1 
                visited[ty] = 1 
                wvalue = maps[tx][ty] + tz  
                for wy, val in enumerate(maps[ty]) :
                    if val != 0 :
                        que.append((ty,wy,wvalue))
            
            else :
                if visited[ty] == 1 and maps[tx][ty] + tz <= k :
                    wvalue = maps[tx][ty] + tz  
                    for wy, val in enumerate(maps[ty]) :
                        if val != 0 :
                            que.append((ty,wy,wvalue))
                    
                
    return  visited, cnt

def solution(N, road, K):
    answer = 1

    road.sort(key = lambda x : x[0])
    
    maps = [[ 0 for i in range(N)] for j in range(N) ]
    willdo = []
    for x,y,z in road :
        if x > y :
            x,y = y, x 
        if maps[x-1][y-1] == 0 :    
            maps[x-1][y-1] = z 
        else :
            if z < maps[x-1][y-1] :
                maps[x-1][y-1] = z 
                
        if x-1 == 0 :
            willdo.append(y-1)
    
    x = 0
    visited = [0 for i in range(N)]
    #visited[0] = 1 
    #print(maps)
    #print(visited)
    for w in willdo :
        visited, val  = willchk(maps, visited, x, w, K)
        answer += val
        #print("xpxxxxxx")
        #print(answer)

    return answer


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
