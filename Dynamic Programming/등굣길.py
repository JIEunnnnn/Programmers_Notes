#LV.3 등굣길
#최단거리를 찾는 문제
#
#처음에 당연히 DFS! 생각을 했는데
#DP이면 점화식이라는 사실을 인지하지 못했다...!!! 
#https://m.post.naver.com/viewer/postView.nhn?volumeNo=26933342&memberNo=33264526

def solution(m, n, puddles):
    answer = 0
    
    maps = [[0 for i in range(m)] for i in range(n)]
    maps[0][0] = 1
    
    for x in range(n) :
        for y in range(m) :
            if x == 0 and y == 0 :
                continue 
            if [y+1,x+1] in puddles :
                maps[x][y] = 0 
            else :
                maps[x][y] += (maps[x-1][y] + maps[x][y-1])
                
    return (maps[-1][-1]) % 1000000007

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
