

#1차시도 => 실패(이게 맞다고 생각했는데...?)
def solution(n, money):
    answer = 0
    
    money.sort()
    
    for i in money :
        if i == 1 :
            answer += 1
            continue 
    
        result = n // i
        others = n % i 
        answer += result 
        if others not in [0,1] :
            for m in money :
                if others < m :
                    break 
                if others % m == 0 :
                    answer += 1 
            
    return answer % 1000000007
  
