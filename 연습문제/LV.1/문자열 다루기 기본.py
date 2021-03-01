#LV.1 문자열다루기 기본 
#주어진문자열길이가 4, 6인지, 숫자로만 구성되어있는지 검사하는 알고리즘
#
#len() 메소드 및 isalpha(). isdigit() 검사하는 메소드 활용 
#

def solution(s):
    
    if not len(s) == 4 or len(s) == 6 :
        return False
    
    for i in s :
        #isalpha(), isdigit()
        # if str(type(a)) == "<class 'str'>" :
        
        if i.isalpha() == True :
            return False
        
    
    return True
