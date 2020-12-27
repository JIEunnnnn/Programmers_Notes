#LV.2 숫자의 표현 
#연속하게 숫자를 더해서 n값을 몇번 나타낼수있는가? 
#
#이중for문돌려서 효율성은 좋지못하겠지...ㅠ 
#가장 신기했던 답은...입력받은 값까지 1부터 홀수로 나누어서 나머지가 0이 되는 갯수로 찾은것...(수학천재들이 많다ㅠ)

def solution(n):
    answer = 0
    
    for i in range(1,n+1) :
        tmp=0
        for j in range(i,n+1):
            tmp+=j
            if tmp==n:
                answer+=1
                break 
            elif tmp>n:
                break
    
    return answer
    
