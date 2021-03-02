#LV.1 정수제곱근판별
#주어진 N이 양의 제곱인지 검사하는 알고리즘
#
#sqrt() 함수활용..!
#

import math 

def solution(n):
    tmp = math.sqrt(n)
    
    #if tmp * tmp == n : => 양의정수를 구해야하는데 이렇게되면 음의정수도 나오잖아^^ 똥멍청이 
    if tmp == int(tmp) : 
        return (tmp+1) * (tmp+1)
    else :
        return -1
