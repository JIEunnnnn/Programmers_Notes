
=============================================================
#1차시도
#정확성오류...40점 

def solution(s):
    s_list = s.split()
    tmp_list = []
    for i in s_list :
        tmp =i[0].upper() + i[1:].lower()
        tmp_list.append(tmp)
        
    return ' '.join(tmp_list)
