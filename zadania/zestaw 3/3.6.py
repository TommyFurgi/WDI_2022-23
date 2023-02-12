def czy_tylko_parzyste(liczba):
    while liczba>0:
        if liczba%2==1:
            return False
        liczba//=10
    return True
t=[1,45,36,7,43,766,12,63,63,43,366]

flaga = 0
for i in t:
    if czy_tylko_parzyste(i):
        flaga=1
        break
if flaga==1:
    print("nie")
else:
    print("tak")