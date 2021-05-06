#Summer,Winter Coding(~2018) 기지국 설치
#
#
#
#

#1차시도 
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
    w_chk = [i for i in range(1, 2 * w + 2 )]
    print(w_chk)    
    
    cnt = 1
    chk = []
    for a in apart :
        #print(w_chk)
        if a not in w_chk :
            cnt +=1 
            abc = 0
            for i,v in enumerate(w_chk) :
                w_chk[i] = a + abc 
                abc +=1 
    
    #print(cnt)
    #print(chk)
    
    return cnt 
    
    
    
    return answer
