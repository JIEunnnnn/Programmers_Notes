#LV.1 가운데글자 가져오기
#주어진 문자열이 홀수냐 짝수냐에 따라 가운데글자 가져오기 
#
#역시레벨원..최고야
#

import math 

def solution(s):
    index = 0
    if len(s)%2 == 0 :
        #짝수일경우 
        index = len(s)-1
        index = int(index/2)
        print(index)
        return s[index :index+2]
        
    else :
        index = int(len(s)/2)
        print(index)
        return s[index]

    
