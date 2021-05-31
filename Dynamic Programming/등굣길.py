
===================================================
#1차시도

#DFS 로 최단경로 찾아야되지? 
import math 

dxys = [(0,1), (1,0)] #오른쪽, 아래쪽 

def solution(m, n, puddles):

    maps = [[0 for i in range(m)] for i in range(n)]
    #print(maps)
    
    for x,y in puddles :
        maps[y-1][x-1] = 1 
    
    #print(maps)
    
    stack = [(0,0, 0)] #x,y, count
    answer = math.inf 
    
    while stack :
        x,y,cnt = stack.pop()
        for dx, dy in dxys :
            tx,ty = x+dx, y+dy 
            if 0<= tx < n and 0<=ty < m : 
                if maps[tx][ty] == 0 :
                    stack.append((tx,ty, cnt+1))
                    
        if x == n-1 and y == n-1 :
            if answer > cnt :
                answer = cnt 

        #print(stack)
        
    return answer%1000000007
