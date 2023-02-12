licznik = 0
n=25
c=1
while c <= n:
    b=c
    while b <= n:
        a=b
        while a <= n:
            licznik+=1
            a*=5
        b*=3
    c*=2
print(licznik)