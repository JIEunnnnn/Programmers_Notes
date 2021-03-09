#Summer/Winter Coding(~2018) 스킬트리
#주어진 skill순대로 학습하지않으면 X
#
#1. 문자열을 리스트화시켜 검사하는 알고리즘으로 구현 
#

#다른사람 풀이 
def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees: 
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0): 
                    break
        else:
            answer += 1

    return answer


def solution(skill, skill_trees):
    answer = 0
    stack = list(skill)
    #print(stack)
    
    for i in skill_trees :
        list_i = list(i)
        #print(list_i)  
        idx = 0
        for j in list_i :
            flag = 0
            if j == stack[idx] :
                if idx == len(stack) -1 :
                    break 
                idx += 1
            else :
                if j in skill :
                    if int(skill.index(j)) - idx >= 1 : 
                                        # 만약, 기존 스킬순서에는 존재하지만, 진행된 index 와 동일하지않으면..  
                                        # 스킬트리가 순서대로임이 아님을 알수있다
                                        # + 스킬순서가 중복되지않는 다는 전제가 있었기에 가능했었던 것 같다.. 
                        #print(i)
                        flag = 1 
                        break 
                        
        if flag != 1 :
            answer +=1 
        #print("테스트")
         

                    
    return answer
  
  
