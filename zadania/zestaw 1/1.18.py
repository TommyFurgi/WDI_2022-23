liczba=6
a=1
b=liczba
e=0.0000000000001
while abs(a-b)>e:
    a = (a*2+b)/3
    b = liczba/a/a

print(a)
