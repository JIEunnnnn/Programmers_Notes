#LV.2 최댓값과 최솟값
#주어진문자열에서 최댓값과 최솟값구하기
#
#내장함수를 사용하기 위해 list변환 및 map()이용해 int변환
#

def solution(s):
    #s_list = s.split()
    
    s_list = list(map(int, s.split()))
    #print(s_list)
    max_value = max(s_list)
    min_value = min(s_list)
    
    
    #print(max_value)
    #print(min_value)
    return str(min_value)+' '+str(max_value)
    
    
