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
