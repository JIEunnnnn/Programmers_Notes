#Summer,Winter Coding(~2018) 기지국 설치
#최소한의 기지국 설치하기 
#
#처음에, 기지국범위에 들지않은 지역을 list화하여 체크함 
#하지만 정확성 및 효율성이 낮... ==> 지역따로따로가 아닌 범위로 체크해야한다는 사실! (접근부터가 틀렸네ㅎㅎ;)
#https://inspirit941.tistory.com/90

import math

def solution(n, stations, w):
    answer = 0
    distance = []
    
    for i in range(1, len(stations)) :
        distance.append((stations[i]-w-1) - (stations[i-1] + w))
        # 9-5 = 범위4
        
        

    #맨 앞 기지국 범위X
    distance.append(stations[0] - w - 1)
    
    #맨 뒤 기지국 범위X 
    distance.append(n - (stations[-1]+w))
    
    #print(distance )
    
    for d in distance :
        if d <= 0 :
            continue 
        answer += math.ceil(d/((2*w)+1)) => # 11  [4, 11]	1	
                                            #distance= [2, 4, -1] 
                                            # 4 / (1*2+1) = 1.33333 ==> math.ceil로 2개 설치해야함을 알수있다.
    
    
    
    return answer

==========================================================
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
