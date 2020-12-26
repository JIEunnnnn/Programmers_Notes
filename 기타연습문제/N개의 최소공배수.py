#LV.2 N개의 최소공배수
#주어진 숫자들의 최소공배수 구하기
#
#최소공배수 = 두개의 곱/최대공약수 
#수학식을 활용하여 for문으로 알고리즘만들었당ㅎ  

from math import gcd #최대공약수

def solution(arr):
    answer = 0
    tmp=0
    
    for i,v in enumerate(arr) :
        if i > 0 :
            tmp = int(v*tmp / gcd(v,tmp))
            answer = tmp
        else :
            tmp = v
    
    return answer
    
