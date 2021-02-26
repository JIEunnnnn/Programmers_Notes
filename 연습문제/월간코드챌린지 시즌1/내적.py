#월간코드챌린지 시즌1 내적.py
#주어진 리스트 a와 b를 곱한 후, 최종합구하기
#
#a와 b가 크기가 동일하므로 for문돌려서 구함(매우매우 쉬웠다!)
#

def solution(a, b):
    
    answer = 0
    for i in range(len(a)) :
        #print(i)
        answer += a[i]*b[i]
    
    
    return answer
