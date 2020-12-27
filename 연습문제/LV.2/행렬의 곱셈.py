#LV.2 행렬의 곱셈 
#2개의 행렬을 곱한값을 출력하는 알고리즘
#
#처음에 아무생각없이 tmp를 둬서 문제를 풀었는데, 2*3, 3*2 같은 행렬을 생각하지않음ㅠ 
#행렬의곱셈 규칙을 생각해서 문제를 풀었다! 
#arr1 : [[1, 2, 3], [4, 5, 6]], arr2 : [[1, 4], [2, 5], [3, 6]] return : [[14, 32], [32, 77]]

def solution(arr1, arr2):
    #print(len(arr2))
    #print(len(arr2[0]))
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    print(answer)
    
    for i in range(len(arr1)) :
        for j in range(len(arr2[0])) :
            for k in range(len(arr2)) :
                answer[i][j] += (arr1[i][k] * arr2[k][j])
    return answer


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
