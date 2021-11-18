

#1차시도 
from collections import deque

def solution(k, dungeons):
    answer = 0 
    
    s_dun = deque(sorted(dungeons, key = lambda x : x[0], reverse = True))
    
    while True :
        if len(s_dun) == 0 :
            break 
            
        if s_dun[0][0] == k :
            tmp = s_dun.popleft()
            k -= tmp[1]

            answer += 1
        elif s_dun[0][0] < k :
            small = min(s_dun, key = lambda x : x[0] < k and x[1])
            if small is None :
                break 
            s_dun.remove(small)
            answer += 1
            
            k -= small[1]
        else :
            s_dun.popleft()
            
    
    
    
    return answer
