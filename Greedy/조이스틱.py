#LV.2 조이스틱 
#주어진 name을 변환시킬때 조이스틱 몇번 움직어야하는가
#
#왼쪽오른쪽 가는것을 고려안함..........;;; 
#left,right 고려하여 작은수를 answer에 더하기 

def solution(name):
    
    name_list = [min(ord(i) - ord('A'), ord('Z')-ord(i)+1) for i in name] #굳이 for문말고...min함수활용하여 작은수구하기 가능...! 
    #위아래 조이스틱횟수 의미
    #print(name_list)
    answer = 0
    idx = 0
    
    #왼쪽오른쪽 
    while True :
        #print("인덱스")
        #print(idx)
        answer += name_list[idx]
        name_list[idx] = 0
        
        if sum(name_list) == 0 :
            return answer 
        
        left, right = 1,1 
        while name_list[idx-left] == 0 : 
                                        #0이 존재하는동안 while문실행 
                                        #[0, 0, 9, 12, 4, 13]
                                        #9를 기준으로 왼쪽 2번이동해서 0을 바꾸는것보다 오른쪽 1번이동해서 12를 바꾸는게 유리함(최소거리)
            #print("레프트")
            #print(name_list)
            left +=1 
        
        while name_list[idx + right] == 0 :
            #print("롸이트")
            #print(name_list)
            right +=1 
            
        answer += left if left < right else right 
        #왼쪽이동수와 오른쪽이동수 중 더 작은것을 더하기
        #동일할경우 아무거나 더해도됨(1,1) -> +1
        
        idx += -left if left < right else right     
        #만약 왼쪽으로 이동할경우 (오른쪽보다 짧아서) -1 부터시행
        #리스트 -1은 맨끝요소 의미함 
    
    
    return answer

===============================================================
#1차시도 
#정확성 54 .... 

def solution(name):
    
    answer = 0

    front = ord('A')
    end = ord('Z')
    
    tmp = 0
    for i in name :
        
        if i == 'A' :
            print(i)
            tmp +=1 
        else :
            if abs(ord(i) - front) > abs(ord(i) - end) :
                print(i)
                print(ord(i))
                answer +=1
                answer += abs(ord(i) - end )
            elif abs(ord(i) - front) < abs(ord(i) - end ) :
                print(i)
                answer += abs(ord(i) - front)
            else :
                print(i)
                answer += abs(ord(i) - front)
    

    answer += len(name)
    answer -= 1 
    answer -= tmp
    
    return answer
