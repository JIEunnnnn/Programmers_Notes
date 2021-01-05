#LV.3 야근지수
#야근 피로도는 야근을 시작한 시점에서 남은 일의 작업량을 제곱하여 더한 값인데, 이 값을 최소값으로 반환시키는 문제
#
#max()는 O(n)이므로 이를 보완하기 위해 heapq모듈 활용, 최소값만 지원하므로 음수를 활용해 구현(어차피 제곱하면 값은 동일하니까!!)
#

import heapq

def solution(n, works):
    
    if n > sum(works) :
        return 0 
    works = [-i for i in works] 
    heapq.heapify(works)
    print(works)
    
    while n > 0 :
        
        heapq.heappush(works, heapq.heappop(works)+1)
        n-=1
        #print(works)
                
        
    print(works)
    answer = 0
    for i in works :
        answer += i**2
    return answer

========================================================================
#2차시도
#효율성 최악...?
#MAX값에서 -1 하는것이 가장 작은 야근지수 찾을수있음 ex) [5,9,13] N=5  

def solution(n, works):
    
    while n > 0 :
    
            if max(works) > 0 :
                idx = works.index(max(works))
                works[idx] = works[idx] - 1
                n-=1
                
            
            else : #max==0일경우 
                return 0
                
    print(works)
    answer = 0
    for i in works :
        answer += i**2
    return answer


#1차시도
#정확성및 효율성...최악^^7 

def solution(n, works):
    
    while n != 0 :
    
        if n >= len(works) :
            for i,v in enumerate(works) :
                works[i] = v-1
            n -= len(works)
            
        
        else :
            if max(works) >= n :
                idx = works.index(max(works))
                works[idx] = works[idx] - n
                n=0
            elif max(works) < n and max(works) > 0 :
                idx = works.index(max(works))
                works[idx] = works[idx] - 1
                n-=1
                
            
            else : #max==0일경우 
                return 0
                
    print(works)
    answer = 0
    for i in works :
        answer += i**2
    return answer
