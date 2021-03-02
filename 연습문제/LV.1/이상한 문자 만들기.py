#LV.1 이상한 문자 만들기
#인덱스 홀짝에 따라 대소문자 구분하는 알고리즘
#
#공백문자라고 명시했으므로 NULL검사X  => if i is None or if not i 체크X ( 문자이므로...) 
#

def solution(s):
    answer = ''
    
    tag = 0 
    #1. s는 모두 대소문자 모두 존재한다.
    #2. s는 띄어쓰기가 1개 이상 있다.
    # 각 단어는 하나 이상의 공백문자로 구분되어 있습니다.
    # => if i is None or if not i 체크X ( 문자이므로...) 


    for i in s :
        #짝수 대, 홀수 소
        
        if i == ' '  :    
            
            answer += ' '
            tag = 0
        
        else :
        
            if tag % 2 == 0 :
                answer += i.upper()
            else :
                answer += i.lower()
            tag +=1 
            
    return answer
    
    
