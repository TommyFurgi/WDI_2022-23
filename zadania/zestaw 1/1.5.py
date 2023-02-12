liczba=2
a=1
b=liczba
e=0.0000001
while abs(a-b)>e:
    a = (a+b)/2
    b = liczba/a

print(a)
