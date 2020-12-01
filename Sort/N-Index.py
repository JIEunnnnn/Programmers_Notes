#LV.2 H-index 
#최대 N개 인용한 N개의 논문구하기 
#
#1차시도시 단순히 정렬하여 중앙값을 구하는 것이라 생각 -> NO 
#N개이상 인용한 N개의 논문이 동일해야한다는 것을 알게 되었다. 
# 1. while-for 문 2중으로 구하니까 list range 초과문제 발생 -> NO
# 2. 전체논문을 기준으로 fiter 메소드 활용하여 N개이상의 논문을 N번인용하는 조건문으로 값찾기  

#어떤 연구자의 h 지수는 그 사람이 쓴 모든 논문 중 n회 이상 인용된 논문이 n개 이상일 때, 이 둘을 동시에 만족하는 n의 최대값으로 한다.

def solution(citations):
    
    H_index = len(citations)
    print(H_index)
    
    for i in range(len(citations))  : 
        #index구할때 유용한방법.. 0부터 len(citations) -1  까지의 값
        #for i in citations : 보통리스트값(value)을 구할때 사용
        
        filter_list = list(filter(lambda x : x >= H_index, citations)) #filter와 lamdbda 활용하여 H__index 이상인 논문갯수 찾기
        
        if H_index != len(filter_list) :
            if H_index < len(filter_list) : #H_index가 작으면 결국 H_index가 최댓값됨ㅇㅇ  [0,0,1,1] -> 1 / [0,0,0,0] -> 0
                break 
            
            H_index -=1
            continue #for문부터 다시시작!
            
        else :
            break

    answer = H_index
    return answer


===============================================================================================
#1차시도

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
