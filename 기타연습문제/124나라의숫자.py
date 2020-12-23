#LV.2 124나라의 숫자
#10진법숫자를 1,2,4만으로 표현하는 알고리즘 구현 
#
#처음헤맨부분은 3진법인거는 알겠는데 0으로 나눠떨어질때 원하는 결과값이 안나옴 => 몫에서 -1함으로써 결과값형성가능
#

def solution(n):
    
    dic = {1 : "1", 2: "2", 0:"4" }
    que = 1 
    remain = 1 
    answer = ''
    
    while que != 0 :
        que = int(n/3)
        remain = int(n%3) 
        
        answer = dic[remain] + answer
        print(answer)        
        
        if remain == 0 :
            que -=1 
        
        n = que
    
    return answer
