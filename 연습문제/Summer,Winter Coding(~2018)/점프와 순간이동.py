#Summer,Winter Coding(~2018) 점프와 순간 이동
#K칸이동시 건전지사용량이 추가되는데 최소한의 에너지만 사용하기 
#
#규칙이 2,4,8,16 에서 1개의 에너지만 사용 
#     => 2와 관련됨을 알수있었다 = 이진법생각해보기!!! 

def solution(n):

    #순간이동(*2)은 건전지X, K칸 점프시 건전지사용량 ㅇㅇ 
    #건전지사용량 최솟값... 
    
    #bin(n)[2:].count('1')
    
    ans = list(format(n, 'b'))
    #print(ans)
    cnt = 0 
    for a in ans :
        if a == '1' :
            cnt +=1 
    return cnt 
  
