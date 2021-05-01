

#1차시도 => 테스트케이스만 통과하는구나....ㅠ
def solution(n, s):
    answer = []
    #N개의 자연수의 합이 S가 되는 집합 
    #곱이 최대여야 함..! => 중간값들을 곱하는 것이.. 최댓값..!
    
    if s % n == 0 : #나눠지는 경우
        tmp = int(s / n) 
        return [tmp] * n     
        
    else :
        tmp = s // n 
        if tmp == 0 :
            return [-1] 
        else :
            for i in range(n) :
                answer.append(tmp)
                tmp +=1 
                
            return answer 
          
