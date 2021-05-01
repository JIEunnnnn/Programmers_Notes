#LV.3 입국심사
#모든 사람이 심사를 받는데 걸리는 시간을 최소값으로 구하는 알고리즘
#
#이분탐색에 대해 제대로 몰랐다...핳..최소-최대로 범위를 점차 좁혀나가야 했던 문제였다..! 
#
#https://inspirit941.tistory.com/153

def solution(n, times):
    answer = 0
    
    left, right = 1, max(times) * n 
    #가장오래걸리는 심사관에게 다 받는 경우 
    #최소-최대범위로 범위를 좁히는 과정... 

    answer = 0 
    while left <= right :
        mid = (left + right) // 2 
        people = 0
        for i in times :
            people += mid // i 

            if people >= n : 
                #심사관이 검사할수있는 인원수가 N보다 많을경우! 
                answer = mid 
                right = mid - 1 
                break 
        
        #모든사람들을 심사할수 없을 경우, 시간 늘리기
        if people < n :
            left = mid + 1 
            
    
    return answer

=============================================
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
  
