#Summer/Winter Coding(~2018) 숫자 게임
#
#
#
#

from collections import deque
def solution(A, B):
    answer = 0
    
    A.sort(reverse = True)
    B.sort(reverse = True)
    deB = deque(B)
    #deB.sort(reverse = True )    
    for i,v in enumerate(A) :
        if deB[0] > v :
            answer += 1
            deB.popleft()
    
    return answer

================================================
#2차시도
def solution(A, B):
    answer = 0
    
    A.sort()
    B.sort()
    
    for i,v in enumerate(A) : # 순서에 맞출필요가 없죠.. 
                              # 왜냐하면, B < A일경우 다음 A순서에서는 B가 더 클 가능성을 염두해야하니까 
                              # 결국 B가 많이 이겨야하니까, 질경우 제일 작은수로 배치하면 되므로.. 이기는 경우만 생각ㄱㄱ
        if v < B[i] :
            answer += 1 
    
    return answer

#1차시도 => 안될걸 알고있었죠... 
from collections import deque
import math 

def solution(A, B):
    answer = 0
    deq_b = deque(B)
    #print(deq_b)
    cnt = 0 
    #ans = math.inf
    
    while True :
        tmp = 0
        if cnt >= len(A) :
            return answer 
        for i,v in enumerate(A) :
            if v < B[i] :
                tmp += 1
        
        if tmp > answer :
            answer = tmp
        
        cnt += 1 
        abc = deq_b.popleft()
        deq_b.append(abc)
        #break 
    
    #answer = ans
    #return answer
