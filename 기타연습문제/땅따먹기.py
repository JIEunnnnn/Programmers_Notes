
===================================================================
#1차시도 => 런타임에러 

def solution(land):
    answer = 0
    delete_index = []
    
    for i in land :

        if len(delete_index) != 0 :
            for j in delete_index :  
                del i[j]
                #del a[a.index(3)]
        
        tmp = max(i)
        answer += tmp
        delete_index.append(i.index(tmp))
    
    return answer
    
    
