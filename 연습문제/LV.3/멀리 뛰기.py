#LV.3 멀리뛰기 
#멀리뛰기에 사용될 칸의 수 n이 주어질 때, 효진이가 끝에 도달하는 방법이 몇 가지인가?
#
#피보나치규칙을 가지고있었다. 점화식을 세우는 것을 고려하면서 풀자!
#1칸일때 -1가지, 2칸 - 2가지, 3칸 -3가지, 4칸 - 5가지, 5칸 - 8가지 

def solution(n):
    if n<3:
        return n
    
    tmp = [0] * (n+1)
    tmp[1] = 1 
    tmp[2] = 2 
    
    for i in range(3, n+1) :
        tmp[i] = tmp[i-1] + tmp[i-2] #피보나치수열..
    
    return tmp[n] % 1234567

==================================================
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
