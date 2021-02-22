#찾아라 프로그래밍 마에스터 게임맵최단거리.py
#(0,0)에서 우축하단까지 가는데 걸리는 칸의 개수구하기
#
#BFS(큐)로 구현해야했으며, 1의 경우에만 cnt +1 시켜야했다. 
#너무어려운 그래프문제.. 다른것들도 풀어봐야지 :)

from collections import deque

def bfs(start, maps) :
    #방문노드
    #위,아래,오른쪽,왼쪽
    #전체움직임횟수
    
    
    dirs = [(0, -1),(0,1), (-1,0),(1,0)]
    queue = deque()
    queue.append(start)
    
        
    while queue :
        #print(queue)
        
        y,x,cnt = queue.popleft()
        maps[y][x] = 0 
        
        for dy, dx in dirs :
            #print(dy,dx)
            
            ny, nx = y+dy, x+dx 
            if ny == len(maps)-1 and nx == len(maps[0])-1 :
            
                #상대편 진영은 우측하단 => maps의 길이에서 -1 
                #print(y,x,cnt)
                
                return cnt +1 
            
            elif 0 <=ny < len(maps) and 0<=nx<len(maps[0]) and maps[ny][nx] == 1:
           
                #0일경우 지나가기X, 1의 경우에만 지나가기 가능
                #더는 지나가지못하도록 0으로 설정
                
                maps[ny][nx] = 0
                queue.append((ny,nx, cnt+1))
                
                
    return -1 
        
    
    


def solution(maps):    
    return bfs((0,0,1), maps)

