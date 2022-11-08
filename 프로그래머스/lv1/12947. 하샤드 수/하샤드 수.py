def solution(x):
    answer = True
    sum = 0
    y = x
    
    while x >= 1:
        sum += x % 10
        x //= 10
    
    if y % sum != 0:
        answer = False
    
    return answer