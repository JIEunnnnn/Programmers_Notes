#LV.1 문자열 내 p와 y의 개수
#주어진 문자열에서 p와 y 개수 찾기
#
#if문활용해서 조건걸고, 리스트컴프레이션 활용해보았다:)
#

def solution(s):
    answer = True
    
    
    count_p = 0
    count_y = 0
    
    for i in s :
        if i == 'P' or i == 'p' :
            count_p +=1
        if i == 'Y' or i == 'y' :
            count_y +=1
            
    if count_p == 0 and count_y == 0 :
        return True 
    else :
        return True if count_p == count_y else False
