liczba = int(input())
a=2
flaga=0
while liczba>77:
    if liczba%a==0:
        flaga=1
        break
    a=3*a+1
if flaga == 1:
    print("Tak")
else:
    print("Nie")
