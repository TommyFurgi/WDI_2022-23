''''1. Dane są dwie tablice t1[N] i t2[N] zawierające liczby naturalne. Z wartości w obu tablicach
możemy tworzyć sumy. „Poprawna” suma to taka, która zawiera co najmniej jeden element
(z tablicy t1 lub t2) o każdym indeksie. Na przykład dla tablic: t1 = [1,3,2,4] i t2 = [9,7,4,8]
poprawnymi sumami są na przykład 1+3+2+4, 9+7+4+8, 1+7+3+8, 1+9+7+2+4+8.
Proszę napisać funkcję generującą i wypisującą wszystkie poprawne sumy, które są liczbami
pierwszymi. Do funkcji należy przekazać dwie tablice, funkcja powinna zwrócić liczbę
znalezionych i wypisanych sum.'''
import math

def is_prime(n):
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0 or n<2:
        return False
    i=5
    while i<math.sqrt(n)+1:
        if n%i==0:
            return False
        i+=2
        if n%i==0:
            return False
        i+=4
    return True

def fun(t1,t2):
    licz=0
    def rek(t1,t2,pos=0,w=[],suma=0):
        if pos==len(t1):    
            if is_prime(suma):
                nonlocal licz
                licz+=1
                print(w)
            return
        return rek(t1,t2,pos+1,w+[t1[pos]],suma+t1[pos]) or rek(t1,t2,pos+1,w+[t2[pos]],suma+t2[pos]) or rek(t1,t2,pos+1,w+[t1[pos]]+[t2[pos]],suma+t1[pos]+t2[pos])
    rek(t1,t2)
    return licz

print(fun([1,3,2,4],[9,7,4,8]))