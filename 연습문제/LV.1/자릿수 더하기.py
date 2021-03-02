#LV.1 자릿수 더하기 
#주어진 int를 각자리숫자를 더하기
#
#형변환 활용해서 총합을 구했다. 
#

def solution(n):
    answer = 0
    
    for i in str(n) :
        answer += int(i)
    

    return answer
