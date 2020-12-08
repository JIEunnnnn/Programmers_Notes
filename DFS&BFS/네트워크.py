# 리트코드 200 

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
