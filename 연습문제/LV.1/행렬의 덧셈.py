#LV.1 행렬의 덧셈
#동일한 행열끼리 더하는 알고리즘
#
#처음 리스트를 arr1크기에 맞게 선언..! 해야했어..!!! 
#다른사람풀이 중 numpy라이브러리활용..이 라이브러리 공부해야겠다..

#다른사람 풀이
import numpy as np

def sumMatrix(A,B):
    A=np.array(A)
    B=np.array(B)
    answer=A+B
    return answer.tolist()
   
   
def solution(arr1, arr2):
    
    answer = [[] for i in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr1[i])) :
            answer[i].append( arr1[i][j] + arr2[i][j])
            
            
    return answer
