#LV.1 자연수 뒤집어 배열로 만들기
#주어진 자연수를 뒤집어서 리스트변환시키는 알고리즘
#
#string 변환후 [::-1]으로 뒤집기! 그후, 리스트에 append()시키기 :) 
#

def solution(n):
    answer = []
    
    tmp = str(n)
    tmp = tmp[::-1]
    
    for i in tmp : 
            answer.append(int(i))
    
    return answer
