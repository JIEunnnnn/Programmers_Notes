#LV.1 체육복
#lost에 따라 체육수업에 참여할수있는 인원수구하기
#
#주어진 배열의 중복값과 lost와 reserve에 해당되는 학생 수 고려해야 함 :)

def solution(n, lost, reserve):
    
    losted = list(set(lost) - set(reserve))
    reserved = list(set(reserve)-set(lost))
    lost = losted
    reserve = reserved
    
            
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
