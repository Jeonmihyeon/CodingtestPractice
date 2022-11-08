def solution(n):
    answer = []
    
    n_str = str(n)
    
    for i in range(1,len(n_str)):
        answer.append(int(n_str[len(n_str) - i]))
    
    answer.append(int(n_str[0]))
    
    return answer