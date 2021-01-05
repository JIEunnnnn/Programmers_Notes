========================================================================
#1차시도
#정확성및 효율성...최악^^7 

def solution(n, works):
    
    while n != 0 :
    
        if n >= len(works) :
            for i,v in enumerate(works) :
                works[i] = v-1
            n -= len(works)
            
        
        else :
            if max(works) >= n :
                idx = works.index(max(works))
                works[idx] = works[idx] - n
                n=0
            elif max(works) < n and max(works) > 0 :
                idx = works.index(max(works))
                works[idx] = works[idx] - 1
                n-=1
                
            
            else : #max==0일경우 
                return 0
                
    print(works)
    answer = 0
    for i in works :
        answer += i**2
    return answer
