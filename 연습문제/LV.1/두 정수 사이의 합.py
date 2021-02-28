#LV.1 두 정수 사이의 합
#주어진 정수사이의 값 더하기
#
# A가 B보다 클때, swap 활용!!
#

def solution(a, b):
    
    if a > b :
        a,b = b,a #swap 

    answer = 0
    for i in range(a,b+1) :
        answer += i 
    
    return answer
