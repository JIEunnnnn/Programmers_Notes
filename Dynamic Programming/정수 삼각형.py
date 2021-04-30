
#1차시도 => 실패
def tri(cnt, ans) :
    abc = []
    for c in cnt :
        tmp = ans + c
        abc.append(tmp)
    return abc

def solution(triangle):
    answer = [triangle[0][0]]
    
    for t in triangle[1:] :
        tmp = []
        for idx, ans in enumerate(answer) :
            #기준점 => idx = 1 일경우, 다음 자리 => idx = 1 or idx = 2 
            
            abc = tri(t[idx:idx+2], ans)
            tmp += abc 
            
        answer = tmp 
        
    #print(answer)  
    
    return max(answer)
