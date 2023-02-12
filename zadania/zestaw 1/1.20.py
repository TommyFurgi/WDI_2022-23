import math
def fun(a,b):
    eps = 1e-6
    while math.abs(a-b)>eps:
        a, b = math.sqrt(a*b), (a+b)/2
    return (a+b)/2
