#LV.2 더 맵게
#주어진 K값보다 작은 스코빌지수를 몇번 계산해야 K값이상의 리스트를 얻을수있는가? 
#
# 1. 계산을 해도 K를 넘지않는 경우(-1) 를 생각해야함 
# 2. 매번정렬하고 최소값 찾아야하기때문에 시간초과발생 => heapq 모듈사용 // 이진트리(binary tree) 기반의 최소 힙(min heap) 자료구조를 제공

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) #기존리스트를 힙으로 변환
    
    while scoville[0] < K :
        answer += 1     
        tmp = heapq.heappop(scoville)
        tmp2 = heapq.heappop(scoville)
        heapq.heappush(scoville ,tmp +tmp2 *2)
        
        if len(scoville) <= 1 and scoville[0] < K : 
            answer = -1
            break

    

    return answer

===================================================================================

#2차시도 => 효율성 시간초과 
def solution(scoville, K):
    answer = 0
    scoville.sort()
    
    while min(scoville) < K :
        answer += 1 
        tmp = scoville.pop(0)     
        tmp2 = scoville.pop(0)
        scoville.append(tmp + tmp2 *2)
        scoville.sort()
        
        if len(scoville) <= 1 and min(scoville) < K : # [0,0,2], 2 -> 결과값 : 2
            answer = -1
            break

    

    return answer
    
#1차시도 => 정확성 및 효율성 시간초과
def solution(scoville, K):
    answer = 0

    filter_scov = list(filter(lambda x : x < K, scoville))
    #K보다 작은 스코빌지수만 모은 리스트 만들어서 풀었던 것때문에 정확성문제가 발생한거같다.
    #ex) [0,0,2] K=2 일경우 [0,0] 형성되어 정확성 오류 

    for i in filter_scov :
        print(i)
        if i < K :
            tmp = i + (i+1)* 2 
            filter_scov.pop(0)
            filter_scov.pop(0)
            filter_scov.append(tmp)
            filter_scov.sort()
            answer +=1
        else :
            break 
        
    if filter_scov[0] < K :
        answer = -1
    #print(filter_scov)

    

    return answer
