#LV.1 최대공약수와 최소공배수
#말그대로, 최대공약수와 최소공배수 구하는 알고리즘
#
#두 자연수의 곱 = 최소공배수 * 최대공약수
#math라이브러리에서는 최대공약수만 제공함(gcd)

import math 
#math는 최대공약수만 제공함! 
#gcd(n,m)


def min(n,m) :
	return n*m // math.gcd(n,m)

def max(n,m) :
	return math.gcd(n,m)



def solution(n, m):
    return [max(n,m),min(n,m) ]
