#LV.2 최솟값만들기
#주어진리스트를 곱해 최솟값만들기
#
#가장큰값*가장작은값이 최솟값을 만들수있는 조건이므로 정렬시켜 알고리즘수행
#

def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    
    for i in range(len(A)) :
        answer += A[i]*B[i]

    return answer
    
    
