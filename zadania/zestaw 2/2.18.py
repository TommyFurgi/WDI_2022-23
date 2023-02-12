a=0
a_next=1
b=2
while True:
    liczba=int(input())
    if liczba==a:
        print(b)
    else: 
        break
    b=b+2*a
    a,a_next=a_next,a_next-b*a