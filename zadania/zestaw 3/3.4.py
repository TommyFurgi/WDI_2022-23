def long_dig(a,b,t):
    for i in range(1,len(t)):
        a*=10
        t[i]+=a//b
        a=a%b
        if a==0:
            return 

def zad4(n):
    digits=[1]+[0]*(n+10)
    fact=1#silnia
    k=1
    while fact<=10**n:
        fact*=k#silnia
        k+=1
        long_dig(1,fact,digits)
        for i in range(len(digits)-1,0,-1): #sprawdzenie czy tablica nie zawiera wartości >10
            digits[i-1]+=digits[i]//10
            digits[i]%=10
    return digits[:n+1]


tab=zad4(1000)
print(tab[0],'.',sep='', end='')
for i in range(1000):
    print(tab[i+1], end='')