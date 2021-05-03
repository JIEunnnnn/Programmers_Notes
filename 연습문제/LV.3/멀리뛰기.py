
#1차시도 시간초과
from itertools import permutations 
from collections import deque 

def solution(n):
    answer = 1 
    
    
    tmp = [1 for i in range(n)]
    tmp_size = len(tmp)
    
    while len(tmp) != 0 :
        tmp = tmp[2:]
        tmp.append(2)
        #print(tmp)
        if sum(tmp) == n :
            
            ing = set(list(permutations(tmp, len(tmp))))
            answer += len(ing)
        
        else :
            
            break 
        
    
    return answer
