#Summer,Winter Coding(~2018) 예산
#주어진 리스트에서 예산내로 최대몇개의 부서를 지원해줄수있는가?
#
#최대로 지원해줄수있는 횟수를 구해야하므로, 오름차순 정렬해서 가장 작은숫자부터..구현! 
#너무 어렵게 생각했나보다...ㅎㅎ;

def solution(d, budget):
    answer = 0
    d.sort()
    
    for cost in d :
        budget -= cost
        answer += 1
        
        if budget < 0: #예산초과할경우 -1
            answer -=1 
            break
            
    return answer


#시간초과발생
def solution(d, budget):
    answer = len(d)
    d.sort(reverse=True)
    
    while True :
        if sum(d) == budget :
            return answer
        elif sum(d) > budget :
            
            if sum(d) - budget in d  :
                d.remove(sum(d) - budget)
                answer -=1
            else :
                d.pop(0)
                answer -=1
            
        
    return answer

#런타임에러 
from itertools import combinations_with_replacement
#중복조합 combinations_with_replacement(반복 가능한 객체, r)
#중복순열 product(반복 가능한 객체, repeat=1)

def solution(d, budget):
    
    d.sort() 
    cnt = 0 
    while True :
        tmp = 0
        for i in d : 
            tmp += i
            cnt += 1 
            if tmp == budget :
                return cnt 
            if tmp > budget :
                break 
        d.pop(0)
        cnt = 0
    
    return cnt
