# https://school.programmers.co.kr/learn/courses/30/lessons/12932
def solution(n):
    answer = []
    
    n_str = str(n)
    
    for i in range(1,len(n_str)):
        answer.append(int(n_str[len(n_str) - i]))
    
    answer.append(int(n_str[0]))
    
    return answer

# 더 짧은 버전 = 아름다운 코드
def solution(n):
    answer = []
    
    n_str = str(n)
    
    for i in range(len(n_str), 0, -1):
        answer.append(int(n_str[i-1]))
    
    return answer
