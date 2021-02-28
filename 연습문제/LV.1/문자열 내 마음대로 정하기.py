




#1차시도 ==> 이게 아닌가봐^^7 

def solution(strings, n):
    answer = {}
    
    for i in strings :
        answer[i[n]] = i
        
    print(answer)
    
    return sorted(answer.keys())
