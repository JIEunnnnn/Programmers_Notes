#LV.2 소수찾기
#주어진 숫자카드로 소수만들기
#
#소수판별은 제곱근활용
#extend()로 리스트 삽입(★☆★append()와는 다름 주의★☆★) 및 set() 로 중복숫자 제거

#순열관련 라이브러리 
#순열은 순서상관O, 조합은 순서상관X

from itertools import permutations 

#제곱근 수행하기 위한 라이브러리 
import math 

def isPrime(ans, size) :  #소수판별하기  
    
    sz =0
    listPrime = []
    while sz < size :
        notPrime = 0
        ans[sz] = int(ans[sz])
        sqrt = int(math.sqrt(ans[sz])+1) #소수판별시 반복문으로 % 연산시 시간초과 => 제곱근으로 소수판별

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
    while mainSz <= len(numbers) : #숫자자리1 -> 숫자자리2 -> 숫자자리3.. 
        perlist = list(map(''.join, permutations(numbers, mainSz )) ) #중복허용X(permutation), 중복허용O(product)
        print(perlist)
        abc = isPrime(perlist, len(perlist))
        listAnswer.extend(abc) #[] 제거없이 데이터들만 받아올수있음
                               #list.append(x)는 리스트 끝에 x 1개를 넣습니다.  ex) [a,b,[a,b]]   
                               #list.extend(iterable)는 리스트 끝에 iterable의 모든 항목을 넣습니다. ex) [a,b,a,b]
        mainSz +=1     
    
    listAnswer = set(listAnswer) #set 으로 중복값제거하기
    print(listAnswer)
    answer= len(listAnswer)

    return answer
