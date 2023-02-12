liczba = int(input())
i=1
a=0
while a < liczba:
    a=i*i+i+1
    if(liczba%a==0):
        print("jest wielokrotnoscia", a, "dla n =", i)
        break
    i+=1