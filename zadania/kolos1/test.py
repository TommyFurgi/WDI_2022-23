import math
def r(l):
    n=int(math.log10(l))
    cyfra=l%10
    return (l%10) * 10**n + l//10
print(r(1234))