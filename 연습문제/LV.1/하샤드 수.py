#LV.1 하샤드 수
#각자리별 더한 숫자가 주어진 수에 나눠떨어지는가? 
#
#
#

def solution(x):
    
    tmp = 0
    for i in list(str(x)) :
        tmp += int(i)
    
    if x % tmp == 0 :
        return True
    else :
        return False
      
      
