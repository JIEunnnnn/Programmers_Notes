#LV.1 시저암호
#주어진 n만큼 이동하여 암호변경
#
#string 라이브러리에 ascii_lowercase, ascii_uppercase 를 제공한다는 사실 알게됨
#isupper(), islower() => 대문자, 소문자인지 검사하는 메소드, bool형식으로 반환
#upper(), lower() => 무조건 대문자, 소문자로 변환하는 메소드 

from string import ascii_lowercase
from string import ascii_uppercase


def solution(s, n):
    answer = ''
    alpha_upper = list(ascii_uppercase)
    alpha_lower = list(ascii_lowercase)
    
    for i in s :
        if i.isupper() :
            tmp =alpha_upper.index(i)
            tmp = tmp+n 
            
            if tmp >= len(alpha_upper) :
                tmp -= len(alpha_lower)
            
            answer+=alpha_upper[tmp]

        elif i.islower() :
            tmp = alpha_lower.index(i)
            tmp = tmp+n 
        
            if tmp >= len(alpha_lower) :
                tmp -= len(alpha_lower)
            
            answer+=alpha_lower[tmp]
        
        else :
            answer+=' '
    
    return answer
