#Summer,Winter Coding(~2018) 기지국 설치
#
#
#
#

def solution(n, stations, w):
    answer = 3
    
    apart  = [i for i in range(1, n+1)]
    for s in stations :
        for w in range(1, w+1) :
            if 0<=s-w <n :
                didx = apart.index(s-w)
                del apart[didx]
            if 0<=s+w<n :
                pidx = apart.index(s+w)
                del apart[pidx]
                
        del apart[apart.index(s)]
        
    print(apart)
    
    for a in apart :
        
    
    
    
    
    return answer
