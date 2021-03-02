#LV.1 정수 내림차순으로 배치하기.py
#주어진 int를 뒤짚어 출력하는 알고리즘
#
#문자열변환 후, sorted 함수 이용 => join 및 int함수로 변환 
#

def solution(n):
    
    answer = []
    for i in str(n) :
        answer.append(i)
    #answer = list(str(n))     
   
        
    #print(answer)
    #print(sorted(answer, key= lambda x : x[0], reverse=True))
    
    answered = sorted(answer, key= lambda x : x[0], reverse=True)
    
    return int(''.join(answered))
    
    
