#LV.2 다음큰숫자
#2진법변환시 1의개수가 동일한 다음 큰숫자 구하기
#
#2진법변환이가능한 bin()내장함수 활용햇으며 굳이 /2하여 계산할필요 없다...(2,8,16진법인경우)
#변환후, count()함수로 1의개수구하기 
#bin(), oct(), hex() <-> int('', 2/8/16)

def solution(n):

    bin_n = bin(n)
    count = bin_n.count('1')
    print(bin_n)
    print(count)  
    while n :
        n+=1 
        bin_tmp = bin(n)
        if bin_tmp.count('1') == count :
            break 
    
    return int(bin_tmp, 2)


