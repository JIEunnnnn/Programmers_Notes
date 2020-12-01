#LV.2 가장큰수
#주어진 숫자를 조합하여 가장 큰 숫자출력하기 
#
# 1. permutations쓰면 시간초과발생 -> NO...
# 2. map() 메소드를 통해 숫자를 문자열(str)로 반환하고 sort() 로 정렬..
#    문자열을 sort()시 아스키코드로 비교하여 정렬 // 몰랐다ㅠㅠ 

def solution(numbers):
    num = list(map(str, numbers))
    num.sort(key =lambda x : x*3, reverse= True) #내림차순정렬, *3하는 이유는 숫자들이 1000이하라고 제한조건ㅇㅇ
    #print(num)
    
    return str(int(''.join(num)))


=====================================================================
#1차시도
import itertools 

def solution(numbers):
    
    size = len(numbers) 
    
    num_list = itertools.permutations(numbers, size)
    sort_num = list(num_list)
    sort_num.sort()
    print(sort_num)
    
    for i in range(len(numbers)) :
        numbers[i]
    
    
    answer = ''
    return answer
