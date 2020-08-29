from itertools import permutations #순열과조합
import math

def isPrime(ans, size) :  #소수판별하기  
    
    sz =0
    listPrime = []
    while sz < size :
        notPrime = 0
        ans[sz] = int(ans[sz])
        sqrt = int(math.sqrt(ans[sz])+1) 

        if ans[sz] == 1 or ans[sz] == 0 :
            notPrime = 1
        else :
            for f in range(2, sqrt , +1):
                if ans[sz] %f == 0:
                        notPrime = 1    
        
        if notPrime == 0 :
            listPrime.append(ans[sz])
            
        sz+=1
        
        
    return listPrime
        


def solution(numbers):
    
    #numbers = [1, 7]
    #numbers2 =[0 ,1, 1]

    mainSz = 1
    listAnswer = []
    answer = 0
    while mainSz <= len(numbers) :
        perlist = list(map(''.join, permutations(numbers, mainSz )) )
        print(perlist)
        abc = isPrime(perlist, len(perlist))
        listAnswer.extend(abc) #[] 제거없이 데이터들만 받아올수있음
        mainSz +=1     
    
    listAnswer = set(listAnswer) #중복값제거하기
    print(listAnswer)
    answer= len(listAnswer)

    return answer
