#LV.2 구명보트
#people 리스트를 옮기는데 걸리는 최소한의 횟수
#
#시도는 거의 유사했으나 pop()으로 인해 시간초과발생함..!
#반드시 pop()이 필요하지않는경우에는 쓰지말자 => 효율성문제!!! 

def solution(people, limit):
    answer = len(people)
    p = sorted(people,reverse = True)
    s,e = 0, len(p)-1
    while s < e : 
        if p[s]+p[e] <= limit :
            e-=1
            answer-=1
        s+=1
    return answer

=========================================================
#1차시도
#효율성 및 정확성... ㅠ 

def solution(people, limit):
    
    people.sort()
    print(people)
    answer = 0
    
    while people :
        if len(people) >= 2 :
            if people[0] + people[1] <= limit :
                answer +=1 
                people.pop(0)
                people.pop(0)
            else :
                answer+=1 
                people.pop(0)
        else :
            answer+=1 
            people.pop(0)
    
    return answer
