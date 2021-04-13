def solution(n, costs):
    answer = 0
    bridge = 0
    
    cycle = {i : i for i in range(n)} 
    #print(cycle)
    costs.sort(key = lambda x : x[2]) #최소비용
    print(costs)
    for i in costs :
        if i[0] > i[1] : #작은번호-큰번호-비용
            i[0], i[1] = i[1], i[0]
            
        if cycle[i[1]] == cycle[i[0]] : #이미 섬끼리 연결됨을 의미함
            continue
            
        answer+= i[2] 
        bridge +=1 #다리 추가
        
        past = cycle[i[1]] #기존 i[1] 을 past에 저장 후 cycle 비교
                           #1-2-3 에서 0-3 추가할경우, past 에 3 : 1 를 저장하고 3 : 0 으로 입력 {0: 0, 1: 1 , 2: 1, 3: 1, 4: 4}
                           #cycle을 for 문을 돌려 1 에 해당되는 값을 가진 key들 업데이트 시키기 
                           # {0: 0, 1: 0 , 2: 0 , 3: 0, 4: 4}
        cycle[i[1]] = cycle[i[0]] #i[1] 과 i[0] 연결 
        
        for k,v in cycle.items() :
            if v == past :
                cycle[k] = cycle[i[0]]
                
        if bridge == n-1 :
            break 
    return answer
