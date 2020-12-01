#어떤 연구자의 h 지수는 그 사람이 쓴 모든 논문 중 n회 이상 인용된 논문이 n개 이상일 때, 이 둘을 동시에 만족하는 n의 최대값으로 한다.




===============================================================================================
def solution(citations):
    
    answer = 0
    mid_value = 0 
    
    citations.sort()
    print(citations)
    
    sz = len(citations) #발표논문
    
    
    if sz % 2 == 1 :
        tmp = int((sz - 1)/2) #중앙자리값찾기       
        print(tmp)
        mid_value = citations[tmp]        
    
    else :
        tmp = int(sz/2)
        mid_value = citations[tmp] 
    
    print(mid_value)
    while sz == 0 :
        
        
        
        
        sz -= 1
        
        
        
    
    return answer
