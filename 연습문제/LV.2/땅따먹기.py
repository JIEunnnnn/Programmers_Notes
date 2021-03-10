#LV.2 땅따먹기
#행렬에서 가장 큰값을 더해 리턴(동일한 열에서는 더하기X) + 열의 값이 4임을 조건으로 제공 
#
#[1,1,99,100][1,1,1,99] 인경우 고려하지 않아 틀린것으로 유추됨
#1행부터 생각하지 말고, 2행부터 더해서 내려가면... max값을 구할수이따.. 논리적사고 필요ㅠㅠ 

def solution(land):
    answer =  0
    #max_land = [0 for i in range(len(land))]
    
    #열은 4까지 주어짐!(조건)
    for i in range(len(land)-1) :
        #print(land)
        land[i+1][0] += max(land[i][1], land[i][2], land[i][3])
        land[i+1][1] += max(land[i][0], land[i][2], land[i][3])
        land[i+1][2] += max(land[i][0], land[i][1], land[i][3])
        land[i+1][3] += max(land[i][0], land[i][1], land[i][2])
        
        #answer += max(max_land)
        #print(max_land)
        
    
    return max(land[len(land)-1])


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
  
  
