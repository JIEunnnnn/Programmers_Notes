#LV.3 다리를지나는 트럭
#정해진 weight이하만 트럭이 다리를 지날수있으며
#건너는데 걸리는 총 시간을 구하는 문제 
#
#처음알고리즘 작성시, 변수를 너무 다양하게 두었으며 필요없는 값까지 구하려했던게 패착
#pop(0)를 활용하여 popleft()처럼 메소드활용할수있다는 것을 깨달음
#또한 매번 전체 bridge_on 리스트 합을 구하는 것은 시간초과문제발생하게 만듦...  

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_on = [0] * bridge_length #다리를 건너는 트럭 최대갯수
    bridge_sum = 0 #다리위총합
    
    while bridge_on : 
    #bridge_on 리스트가 비어있으면 반복문 종료.. 
        answer+=1
        tmp = bridge_on.pop(0)
        bridge_sum -= tmp
        if truck_weights : #대기트럭이 존재한다면 
            
            #if sum(bridge_on) + truck_weights[0] <= weight :
            if bridge_sum + truck_weights[0] <= weight :
                bridge_on.append(truck_weights[0])
                bridge_sum +=truck_weights[0]
                truck_weights.pop(0)
                #print(bridge_on)
            
            
            else :
                bridge_on.append(0)
                #print(bridge_on)
                
            if bridge_sum == 0 and len(truck_weights) == 0:
                break
    
    return answer
