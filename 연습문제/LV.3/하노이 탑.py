#LV.3 하노이 탑
#n개의 원판을 3번 원판으로 최소로 옮기는 방법
#
#프로그래머스랑 동일한문제! 
#재귀를 활용하여, 알고리즘 구현해야함!! 

def solution(n):
    answer = [] 
    
    def hanoi(n, start, end, assist):
        nonlocal answer
        if n == 1: # 원판이 1개면 재귀 종료
            answer.append([start, end])
            return
        hanoi(n-1, start, assist, end) 
        answer.append([start, end])
        hanoi(n-1, assist, end, start)
        
    hanoi(n, 1, 3, 2) 
    return answer
  
