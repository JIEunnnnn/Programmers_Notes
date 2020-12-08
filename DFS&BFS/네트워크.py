#LV.3 네트워크 
#주어진리스트에 따라 연결해야할 네트워크 수 구하기
#
#경로만 알면 되므로 =>  BFS(큐)

#리트코드 200 

def solution(n, computers):
    
    answer = 0
    visited = [0]*n #방문노드(방문하면=1)
    bfs = [] #경로노드(큐)
    print(visited)
    
    while 0 in visited : #방문하지않는 노드가 존재하지않을때까지 
        
        start = visited.index(0) #리스트의 value(0)통해 KEY찾기
        bfs.append(start) #시작노드 
        visited[start] = 1 
        
        while bfs : #큐(bfs)에 값이 존재하면 계속 실행
            node = bfs.pop(0)
            for i in range(n) :
                if visited[i] == 0 and computers[node][i] == 1:
                #방문하지않은 노드이며 연결되어있을 경우
                    bfs.append(i)  #방문한 노드부터 다시시작
                    visited[i] = 1 #방문했다
                
        answer +=1 #큐에 값이없이없을경우 +1 ==> 연결된 노드 다찾았으며 다시 방문하지않은 노드부터 연결고리 찾기       
                
    return answer

=============================================================
#1차시도
#정확성 실패
#return = 전체노드 수 - 연결 간선수 
#         n - sum(computers)
import math

def solution(n, computers):
    sum = 0
    
    for i,v in enumerate(computers) : #index
        for j,k in enumerate(v) :
            if i != j :
                sum += k
                

    #print(sum) 
    #print(int(sum/2))
    answer =  n - math.ceil(sum/2) 
    #answer = 0
    return answer
