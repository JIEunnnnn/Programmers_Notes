#LV.1 제일작은 수 제거하기
#주어진리스트에서 가장 작은값제거하는 알고리즘
#
#리스트 내장함수활용..
#

def solution(arr):
    
    if len(arr) == 1 :
        return [-1] 
    else :
        min_value = min(arr)
        print(min_value)
        tmp = arr.index(min_value)
        
        del arr[tmp]
    
    return arr
