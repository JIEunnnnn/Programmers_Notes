#LV.1 수박수박수박수박수박수?
#주어진 자연수에 따라 수박*n 반복하는 문제
#
# flag활용해서 문자열 다르게 설정했다! 
#

def solution(n):
    answer = ''
    flag = 0
    for i in range(n) :
        if flag == 0 :
            answer += '수'
            flag = 1
        else :
            answer += '박'
            #answer.append('박') 리스트 더할때..! 
            flag = 0
    
    #''.join(answer) 리스트에서 문자열 변환시사용하는 메소드
    #list = str.split(공백기준) : 문자열 => 리스트, 공백시 스페이스 기준
    
    return answer
  
  
