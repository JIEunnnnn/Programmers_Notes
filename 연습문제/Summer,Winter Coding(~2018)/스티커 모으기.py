#Summer/Winter Coding(~2018) 스티커 모으기(2)
#이웃하지않은 스티커 최대합 구하기
#
#점화식 + 첫번째 스티커 고려를 통해.... 해결ㅠㅠㅠㅠ (어려워)
#https://bladejun.tistory.com/144

def solution(sticker):
    answer = 0
    
    if len(sticker) <=3 :
        return max(sticker)

    # 1. 첫번째 숫자를 더할때 
    dp=[i for i in sticker]
    dp[1]=0
    dp[2]+=sticker[0]
    
    for idx in range(3,len(sticker)-1):
        dp[idx]+=max(dp[idx-2],dp[idx-3])
    answer=max(dp)
    
    # 2. 두번째 숫자를 더할때 
    dp=[i for i in sticker]
    dp[0]=0
    #print(dp)
    
    for idx in range(3,len(sticker)):
        #dp[idx]= sticker[idx] + max(dp[idx-2],dp[idx-3])
        dp[idx]+=max(dp[idx-2],dp[idx-3])
        #print(dp)

    return max(answer,max(dp))
    
