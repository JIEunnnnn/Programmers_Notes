#LV.1 문자열내림차순으로 배치하기
#주어진문자열을 내림차순으로 배치
#
#문자열 => 리스트 변경하여 sort시킨 후 join으로 문자열복구
#

def solution(s):
    
    tmp = []
    for i in s :
        tmp.append(i)
    # tmp = list(s)
    
    tmp.sort(reverse=True)
    #print(tmp)
    
    return ''.join(tmp)

