def solution(s):
    alpha = "0123456789"
    count = 0
    if len(s) == 4 or len(s) == 6:
        for i in range(0,len(s)):
            if s[i] in alpha:
                count += 1
                
    if count == len(s):
        return True
    else:
        return False
    