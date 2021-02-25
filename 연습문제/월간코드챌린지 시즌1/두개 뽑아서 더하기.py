#월간코드챌린지 season.1 두개뽑아서더하기
#주어진리스트 중 2개를 뽑아 더한수를 내림차순으로 정렬하기
#
#조합을 활용하여 구현 + 리스트에 append 및 정렬하여 구현
#

from itertools import combinations

def solution(numbers):
    answer = []
    
    numlist = list(combinations(numbers, 2))
    #print(numlist)
    
    for i in numlist :
        tmp = i[0]+i[1]
        #print(tmp)
        answer.append(tmp)
        
    
    answer = list(set(answer))
    answer.sort()
    
    #print(answer)
        
    return answer
