

#1차시도 => 시간초과발생!
import heapq

def solution(n, times):
    answer = 0
    
    people = [0 for i in range(n)]
    
    
    cnt = 0 
    heapq.heapify(times)
    #print(times)
    
    dic_times = {}
    for t in times :
        if t not in dic_times :
            dic_times[t] = t 
        else :
            dic_times[t] += t 
    
    while 0 in people  :
        tmp = heapq.heappop(times)
        for idx, val in dic_times.items() :
            if tmp == val :
                tmp2 = tmp + idx 
                dic_times[idx] = tmp2
                
            
        people[cnt] = tmp 
        cnt +=1 
        #tmp2 = tmp + tmp 
        heapq.heappush(times, tmp2)
        #print(people)
        #print(times)
        
    
    #print(people)
        
    
    return people[-1]
  
