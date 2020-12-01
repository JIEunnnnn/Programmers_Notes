

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
