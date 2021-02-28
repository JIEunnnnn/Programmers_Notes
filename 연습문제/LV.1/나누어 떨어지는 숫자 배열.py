#LV.1 나누어떨어지는 숫자배열
#주어진배열에서 divisor으로 나눠지는 리스트구하기
#
#오름차순이기때문에, sort()활용!! 
#

def solution(arr, divisor):
    
    answer = []
    arr.sort()
    for i in  arr :
        if i % divisor == 0 :
            answer.append(i)
    
    if len(answer) == 0 :
        return [-1] 
    
    return answer
  
