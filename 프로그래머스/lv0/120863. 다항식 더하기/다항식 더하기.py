def solution(polynomial):
    answer = ''
    poly = ''
    Coef = 0        #계수
    Con = 0         #상수
    remove_set = {'+'}
    
    polynomial = polynomial.split()
    polynomial = [i for i in polynomial if i not in remove_set]    

    for i in range(0,len(polynomial)):
        if 'x' in polynomial[i]:
            if(len(polynomial[i]) == 1):
                Coef += 1
            else:
                Coef += int(polynomial[i].replace('x',''))
        else:
            Con += int(polynomial[i])
            
            
    if Coef == 0:
        return str(Con)    
    elif Coef == 1:    
        if Con == 0:
            answer = 'x'    
        else:
            answer = 'x ' + '+ ' + str(Con)
    

    else:
        if Con == 0:
            answer = str(Coef) + 'x'    
        else:
            answer = str(Coef) + 'x ' + '+ ' + str(Con)
    
    return answer
        
