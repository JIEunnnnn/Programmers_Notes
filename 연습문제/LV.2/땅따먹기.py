

#1차시도 : 정확성 및 시간초과 발생^^7 
def solution(land):
    answer = 0
    
    idx = 0
    for i in land :
        tmp = max(i)
        if idx != 0 :
            if idx == i.index(tmp) :
                i.pop(i.index(tmp))
                #break 
                
        idx =  i.index(max(i))
            
        answer += max(i)
        
    

    return answer
  
  
