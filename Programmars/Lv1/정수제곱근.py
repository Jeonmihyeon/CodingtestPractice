
# https://school.programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    answer = 0
    a = 1
    while a*a <= n:
        if a*a == n:
            return (a+1)*(a+1)
        a += 1
    return -1
