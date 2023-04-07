import math

def lcm(a, b):
    return (a * b) // math.gcd(a,b)

def solution(numer1, denom1, numer2, denom2):
    answer = []
    denom = lcm(denom1, denom2)
    
    de1 = denom // denom1
    de2 = denom // denom2
    numer = (numer1 * de1) + (numer2 * de2)
    
    
    
    if(math.gcd(numer,denom) != 1 ):
        print (denom)
        print(math.gcd(numer,denom))
        num = numer // math.gcd(numer,denom)
        den = denom // math.gcd(numer,denom)
        answer.append(num)
        answer.append(den) 
    else:
        answer.append(numer)
        answer.append(denom) 

    
    return answer