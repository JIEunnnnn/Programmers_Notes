#LV.2 기능개발
#남은작업(100 - progresses) 처리일 횟수구하기 
#
#정확성문제 => 테스트케이스 추가 [99, 1, 99, 1][1, 1, 1, 1] 결과 :[1, 3]

import math

def solution(progresses, speeds):
    ans_dct = {}
    tag = 0 
    for i in range(len(progresses)) :
        prog = 100 - progresses[i]
        spd = math.ceil(prog / speeds[i]) #처리일 올림구하기
                  
        
        if spd not in ans_dct : 
            if spd < tag and tag !=0 :
                print(tag)
                ans_dct[tag] += 1 
            else :
                print(tag)
                tag = spd
                ans_dct[spd] = 1 
        else : 
            if spd < tag : # 현재작업 일자 < 전 작업의 일자 => 전작업일자 +=1
                ans_dct[tag] +=1
            else :    
                ans_dct[spd] +=1 
    
    answer = []
    for i,v in ans_dct.items() : #key-values
        answer.append(v)
        
    return answer
