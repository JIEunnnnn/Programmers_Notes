#LV.2 주식가격
#가격하락에 따른 시간변화출력하기
# 
#deque사용하니까 효율성문제발생 -> 이중for문으로 변경

def solution(prices):
    answer = [0] *len(prices)
    
    for i in range(len(prices)) :
        tag = prices[i] 
        for j in range(i+1, len(prices)) : #tag 다음주식가격부터 비교하기
            answer[i]+=1 #시간더하기
            if tag > prices[j] :
               break 
                  
    return answer


======================================================================
#시간초과발생 => pop()&deque() 사용시 효율성 ZERO

from collections import deque 

def solution(prices):
    price_dq = deque(prices)
    answer = []
    
    sz = len(price_dq) -1
    for i in range(len(price_dq)) :
        flag = 0
        tag = price_dq.popleft()
        for j in range(len(price_dq)) :
            if tag > price_dq[j] :
                flag = 1
                answer.append(j+1)  
                break
               
        if flag != 1 : 
            answer.append(sz - i)       
                  
    return answer
