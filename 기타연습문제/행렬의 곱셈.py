
======================================================================
#1차시도 => 정확성 0점...
#두 행렬의 크기가 AxB, CxD인 행렬을 곱할려면 B와 C가 같아야 합니다.

def solution(arr1, arr2):
    answer = []    
    for i in range(len(arr1)) :
        tmp_list=[]
        for j in range(len(arr2)) :
            tmp=0
            k=0
            while tmp<len(arr2):
                k += arr1[i][tmp]*arr2[tmp][j]    
                tmp+=1
            tmp_list.append(k)    
        answer.append(tmp_list)
    return answer
