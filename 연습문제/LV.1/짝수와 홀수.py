#LV.1 짝수와 홀수
#주어진 숫자 짝수인지, 홀수인지? 
#
#
#

def solution(num):
    
    if num % 2 == 0:
        return "Even"
    else :
        return "Odd"
      
#불(bool) 자료형 : 참(True)과 거짓(False)의 두 가지 값을 가지고 있는 자료형

        #   참 : 1 , 비어있지 않은 문자열,리스트, 튜플 딕셔너리 등등 (ex. python, [1,2,3])
        #   거짓 : 0, None, 비어있는 문자열, 리스트, 튜플, 딕셔너리 등 ("", [], (), {})
        #   if num % 2 : return "Odd" 
        
