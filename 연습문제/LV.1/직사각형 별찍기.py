#LV.1 직사각형 별찍기
#별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태출력
#
#
#

a, b = map(int, input().strip().split(' '))

for i in range(b) :
       print("*"*a)

#print(("*"*a+'\n')*b)
