def solution(s):
    answer = True
    p_cnt = 0
    y_cnt = 0
    
    for i in s:
        if  'p' == i or 'P' == i:
            p_cnt += 1
        elif 'y' == i or 'Y' == i:
            y_cnt += 1
        
    print(p_cnt, y_cnt)   
    
    if p_cnt != y_cnt:
        answer = False
        
    return answer