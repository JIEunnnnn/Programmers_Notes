# 리트코드 200 

#경로만 알면 되므로 =>  BFS(큐)


def solution(n, computers):
    
    answer = 0
    visited = [0]*n #방문노드
    bfs = []
    print(visited)
    
    while 0 in visited :
        print("테스트중")
        
        start = visited.index(0)
        bfs.append(start)
        visited[start] = 1 
        
        while bfs : #큐에 값이 존재하면 계속 실행
            node = bfs.pop(0)
            for i in range(n) :
                if visited[i] == 0 and computers[node][i] == 1:
                    bfs.append(i)
                    visited[i] = 1 
                    #재귀적으로 풀어야함..? 
                
        answer +=1        
                
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
