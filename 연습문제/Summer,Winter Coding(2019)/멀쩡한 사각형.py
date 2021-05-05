#Summer/Winter Coding(2019) 멀쩡한 사각형
#직사각형을 반으로 자를때, 멀쩡한 사각형의 개수 구하기
#
#처음에, answer = (w*h) - (2w) 로 생각함 
#하지만, 최소공배수만큼을 빼는 규칙이 있다는 것을... 알게되었다..!!(이것은 알고리즘인가 수학문제인가..) 


from math import gcd 

def solution(w,h):
    
    tmp = gcd(w,h)
    answer = (w * h) - (w + h - tmp)
    
    return answer
  
