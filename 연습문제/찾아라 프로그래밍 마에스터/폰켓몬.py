#찾.프.마 폰켓몬
#nums/2의 폰켓몬을 갖거나 각기 다른종류의 폰켓몬 갖기
#
#딕셔너리 활용해서 중복되는 폰켓몬 구별
#

def solution(nums):
    #sz = len(nums)
    #print(sz//2) 정수형으로 반환하는 나눗셈
    
    dic_nums = {i : 0 for i in nums}
    
    tmp = len(nums)//2
    tmp_dic = len(dic_nums)
    
    if tmp == tmp_dic :
        return tmp_dic
    
    elif tmp < tmp_dic :
        return tmp 
    
    else :
        return tmp_dic 
      
      
    
    
