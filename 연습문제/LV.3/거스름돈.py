#LV.3 거스름돈 
#N원을 거스르는 경우의 수 구하기
#
#블로그 참고;; 
#https://velog.io/@younge/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B1%B0%EC%8A%A4%EB%A6%84%EB%8F%88-%EC%97%B0%EC%8A%B5%EB%AC%B8%EC%A0%9CDP

from collections import defaultdict

def solution(n, money):
    dp=defaultdict(int) 
    dp[0]=1
    print(dp)
    for m in money:
        for i in range(m,n+1): #거슬러야할 금액 N까지
                               #m보다 작은경우 고려X - 적재형식이니까
                
            dp[i]+=dp[i-m]%1000000007
            #1원일때, 1가지
            #2원일때, 기존1가지(1원) + 2원1개일때, 2원2개일때
            #5원일때, 3가지 + 5원1가지일때 

            
    return dp[n]

=============================================================
#1차시도 => 실패(이게 맞다고 생각했는데...?) 
#[1,2,5,10] 10 

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
  
