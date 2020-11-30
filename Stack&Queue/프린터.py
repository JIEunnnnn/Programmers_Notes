def solution(priorities, location):
    
    answer = 0
    priority = []
    priority = priorities
    size = len(priority) -1  
    
    sort_priority = sorted(priority, reverse=True)  
        
    while priority :
        
        
        if priority[0] != sort_priority[0] :
            tmp =priority.pop(0)
            priority.append(tmp)
             
            if location == 0 :
                location += size
            else :
                location -=1
            
               
                
        else :
            priority.pop(0)
            sort_priority.pop(0)
            answer+=1
            
            if location == 0 :
                break 
                
            location -=1
    

    return answer
