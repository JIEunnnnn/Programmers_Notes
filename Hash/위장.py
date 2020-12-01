#LV.2 위장
#주어진 아이템에 따라 입을수있는 경우의수 따지기
#
#Counter 라이브러리로 리스트의 동일타입을 딕셔너리(key-value) 형태로 반환(갯수구하기)
#아이템 미착용 경우까지 포함하여 곱셈수행 => 아예 안입는경우 -1 

from collections import Counter #딕셔너리형태 중복키 저장 안됨 -> 갯수비교시 Counter 사용하기 

def solution(clothes):
    answer = 1
    clothesDict = Counter([x[1] for x in clothes]) #딕셔너리형태로 자료개수 구하기
                                                   #x[1] 은 clothes[x][1] 의미 ㅇㅇ
    print(clothesDict) #{'headgear': 2, 'eyewear': 1}
    for v in clothesDict.values():
        answer *= (v+1)  #의상종류 별 의상수에 그 의상을 안 입는 경우의 수도 포함하여 계산하기...ㅠ
    answer -= 1 #아예 입지않는 경우
    return answer
    
======================================================================================================
 #1차시도
 #기존 내 풀이과정.. 
 #counter 라이브러리 생각하지 않고 직접적으로 알고리즘 작성
 #그 후 경우의 수는 어떻게 두어야할지 문제해결불가ㅠㅠ
 
def solution(clothes):
    
    sz = 0 
    clothesDict = dict() #딕셔너리생성하기
    for sz in range(len(clothes)) :     
        if sz == 0 :
            #print(clothes[sz][1])
            clothesDict[clothes[sz][1]] = 1 
        else :
            #딕셔너리 키값과 비교하기
            if clothes[sz][1] in clothesDict.keys():
                    clothesDict[clothes[sz][1]] += 1
                    print(clothesDict)
            else :
                    clothesDict[clothes[sz][1]] = 1
                    print(clothesDict)
                
            
        
        sz +=1 
    answer = 0
    #딕셔너리 키값이 2개이상이면 순열계산수행하여 더하기 
    
    if len(clothesDict) == 1 :
        print(len(clothesDict))
        answer = list(clothesDict.values())
        answer = answer[0]
    else :
        while 
        
        
    len(clothesDict) 
    
    return answer
    
