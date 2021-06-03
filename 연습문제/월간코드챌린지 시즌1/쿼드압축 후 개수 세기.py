#월간 코드 챌린지 시즌1 쿼드압축 후 개수 세기
#하나라도, 좌표가 다를경우 압축불가능한 압축단계...
#
#재귀로 풀어야했는데.. 접근자체를 하는과정이 어려워서 블로그참고 :(
#https://deok2kim.tistory.com/212

def solution(arr):
    answer = [0,0]
    
    n = len(arr)
    
    
    def quart(x,y, n) :
        print(x,y,n)
        init = arr[x][y]
        for i in range(x, x+n) :
            for j in range(y, y+n) :
                if arr[i][j] != init : #값이 다를경우 압축불가능
                    nn = n//2
                    quart(x,y, nn)
                    quart(x,y+nn, nn),
                    quart(x + nn, y, nn)
                    quart(x+nn, y+nn, nn)
                    return
                
        answer[init] +=1 
    
    
    quart(0,0,n)
    return answer
