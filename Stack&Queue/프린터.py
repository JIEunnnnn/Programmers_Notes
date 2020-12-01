#LV.2 프린터
#주어진 우선순위에 따라 지정된위치에서 몇번째로 프린터되는가?
#
#왜 정확성에서 오류가 났는가? 
# 1. 내림차순으로 정렬한게 용량많이 차지한건가? -> NO
# 2. if문마다 pop하고 append한것에서 문제있는건가? -> NO
# 3. 처음에 size를 지정하는게 아니라 pop한후의 priorities 크기가 다르니까 이걸 고려해야하는구나!!

def solution(priorities, location):
    
    answer = 0
    #size = len(priorities) -1  
    #sort_priority = sorted(priorities, reverse=True)  
        
    while priorities :
        max_pri = max(priorities)
        now_pri = priorities.pop(0)
        if location == 0 :
            if now_pri < max_pri :
            #if priorities[0] != sort_priority[0] :
                #tmp =priorities.pop(0)
                priorities.append(now_pri)
                location = len(priorities) -1  ##여기를 고려안한게 주 원인##
            else :
                #priorities.pop(0)
                answer+=1
                break
        else :
            if now_pri < max_pri :
            #if priorities[0] != sort_priority[0]:
                #tmp =priorities.pop(0)
                #priorities.append(tmp)
                priorities.append(now_pri)
                location -=1
            else :
                #priorities.pop(0)
                #sort_priority.pop(0)
                answer+=1
                location -=1
            
    

    return answer


==================================================================================
#1차시도
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
