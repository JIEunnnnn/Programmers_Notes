#LV.1 콜라츠 추측
#최종 숫자가 1이나오게끔 만드는 알고리즘
#
#1일경우를 생각안해서... 테스트케이스 13번 오류떴었ㄷ...
#

def solution(num):
    cnt = 0
    
    if num == 1 :
        return 0 
    
    while True :
        if num%2 : #홀수(1은 True이므로)
            num = num*3 +1 
        else :
            num = num/2 
        cnt +=1
        
        if num == 1:
            return cnt
        
        if cnt >= 500 :
            return -1
