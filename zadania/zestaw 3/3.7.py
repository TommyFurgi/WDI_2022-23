import random
def czy_nieparzyste(liczba):
    while liczba>0:
        if liczba%2==0:
            return False
        liczba//=10
    return True
n=int(input())
t=[0]*n
for i in range(n):
    t[i]=random.randint(1,1000)
    if czy_nieparzyste(t[i]):
        print("istnije ", t[i])
        break

print(t)