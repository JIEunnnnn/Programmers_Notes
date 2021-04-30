#LV.3 정수 삼각형
#삼각형경로에서 더한값중 최댓값 구하기!
#
#1차시도 때, 오류났던것은 덧셈 시, 1 => 2 => 4 => 8 형태....
#그러므로, 중간값을 비교하여 최댓값만 처리하게 끔 알고리즘 변경 

from copy import deepcopy
from collections import deque 

def dfs(tri, cnt) :
    tri = deepcopy(tri)
    tmp = deque()
    
    for idx, v in enumerate(cnt) :
        if len(tmp) > 0 : ####중간값 처리시##### 
            abc = v + tri[idx] 
            if tmp[-1] < abc :
                tmp.pop()
                tmp.append(abc)
        else :
            tmp.append(v+tri[idx])
            
        tmp.append(v+tri[idx+1])
          
    return tmp 


def solution(triangle):
    answer = 0
    cnt = 0 
    tri = [triangle[0][0]]
    for i in triangle[1:] : 
        #print(tri)
        tri = dfs(i, tri)

    answer = max(tri)     
    
    return answer

=======================================================
#1차시도 => 실패
def tri(cnt, ans) :
    abc = []
    for c in cnt :
        tmp = ans + c
        abc.append(tmp) #그냥 더하면 안되요 :) 
    return abc

def solution(triangle):
    answer = [triangle[0][0]]
    
    for t in triangle[1:] :
        tmp = []
        for idx, ans in enumerate(answer) :
            #기준점 => idx = 1 일경우, 다음 자리 => idx = 1 or idx = 2            
            abc = tri(t[idx:idx+2], ans)
            tmp += abc 
            
        answer = tmp 
        
    #print(answer)  
    
    return max(answer)
