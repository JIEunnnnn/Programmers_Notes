def solution(n, costs):
    answer = 0
    bridge = 0
    
    cycle = {i : i for i in range(n)} 
    #print(cycle)
    costs.sort(key = lambda x : x[2])
    print(costs)
    for i in costs :
        if i[0] > i[1] : #작은번호-큰번호-비용
            i[0], i[1] = i[1], i[0]
            
        if cycle[i[1]] == cycle[i[0]] :
            continue 
            
        print(cycle)
        print(cycle[i[0]])
        print(cycle[i[1]])
            
        answer+= i[2]
        bridge +=1 #다리 추가
        
        past = cycle[i[1]]
        cycle[i[1]] = cycle[i[0]]
        
        for k,v in cycle.items() :
            print("ㅌㅌㅌㅌㅌ")
            print(past)
            print(v)
            if v == past :
                cycle[k] = cycle[i[0]]
        if bridge == n-1 :
            break 
    return answer
