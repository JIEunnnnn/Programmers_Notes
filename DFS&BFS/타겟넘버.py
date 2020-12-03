#LV.3 타겟넘버
#주어진 numbers 전체수를 +-하여 target 숫자 맞추기
#
#진짜어려워서... 다른사람 풀이를 참고함ㅠ 
# DFS 를 활용하여 각각 +-시키는 구조로 프로그램을 짰다...

def solution(numbers, target):
    trr = [0]
    for num in numbers :
        sub_trr = []
        for sub in trr :
            sub_trr.append(sub + num) #기준에서 +-num 시키기
            sub_trr.append(sub - num)
        trr = sub_trr
    answer = trr.count(target)
    return answer
