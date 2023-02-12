n=int(input())
a=1
b=1
suma=0
while suma < n:
    suma+=a
    a, b = b, a+b

a=1
b=1
while suma>n:
    suma-=a
    a, b = b, b+a
if suma==n:
    print("istnieje")

