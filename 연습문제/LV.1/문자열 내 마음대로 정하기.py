#LV.1 문자열내마음대로정하기
#주어진 n에 따라 문자열 오름차순으로 정렬! 
#
#딕셔너리와 리스트 활용해서 정렬... + 람다..  
#

#다른사람풀이
def solution(strings, n):
    return sorted(strings, key=lambda x:x[n]+x[:])
    #리스트의 n번먼저 고려하고, 나머지를 정렬고려!! 
    #x[:] = 슬라이싱기법 중 하나로 리스트 전체 요소 가져오는 것의미
    #my_list[시작:끝:스텝] : 스텝은 건너뛰는 것 의미, 끝이 -1 이면 마지막요소 앞을 가리키므로 끝에서 2번째까지 출력

def solution(strings, n):
    answer = []
    tmp = {}
    strings.sort()
    
    #print(strings)
    
    for i in strings :
        tmp[i] = i[n]
        
    #print(tmp)
    abc = sorted(tmp.items(), key=lambda x:x[1])
    #print(abc)

    for i in abc : 
        answer.append(i[0])
    
    return answer

============================================================
#1차시도 ==> 이게 아닌가봐^^7 

def solution(strings, n):
    answer = {}
    
    for i in strings :
        answer[i[n]] = i
        
    print(answer)
    
    return sorted(answer.keys())
