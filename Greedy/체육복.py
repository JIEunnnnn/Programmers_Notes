

==========================================================
#1차시도
#정확성 오류! 

def solution(n, lost, reserve):

    for i in reserve :
        if i in lost :
            reserve.remove(i)
            lost.remove(i)
            
            
    answer = n - len(lost)
    
    while lost :
        tmp = lost.pop(0)
        if tmp-1 in reserve :
            answer +=1 
            reserve.remove(tmp-1)
            continue
        if tmp+1 in reserve :
            answer +=1 
            reserve.remove(tmp+1)
            continue
            
        
    
    return answer
