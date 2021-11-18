#LV.2 모음사전
#
#규칙을 찾아, 딕셔너리로 정의하고 순서구하는 문제 

def solution(word):
    answer = 0 
    dic = {"A" : [1,1,1,1,1], "E" : [782, 157 ,32,7,2],
           "I" :[1563, 313, 63,13,3] , "O" : [2344, 469, 94, 19,4],
           "U" :[3125, 625,125,25 ,5]}

    
    for idx, key in enumerate(word) :
        
        answer += dic[key][idx]
        
    
    return answer
