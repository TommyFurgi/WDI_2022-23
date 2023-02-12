'''
Dana jest liczba naturalna N. Proszę zaimplementować funkcję divide(N), która sprawdza czy jest możliwe
pocięcie liczby N na kawałki, tak aby każdy z kawałków był liczba pierwszą oraz liczba kawałków też była
liczbą pierwszą. Funkcja powinna zwracać wartość logiczną. Na przykład: divide(2347)=True, podział na
23 i 47, natomiast divide(2255)=False.
Przykładowe wywołania funkcji:
print(divide(273)) # True, podział 2|7|3
print(divide(22222)) # True, podział 2|2|2|2|2
print(divide(23672)) # True, podział 23|67|2
print(divide(2222)) # False
print(divide(21722)) # False
'''
import math
def czy_pierwsza(liczba): 
    if liczba == 2 or liczba == 3:
        return True
    if liczba %2 == 0 or liczba%3==0 or liczba<=1:
        return False
    i=5
    while int(math.sqrt(liczba))+1>i:
        if liczba%i == 0:
            return False
        i+=2
        if liczba%i == 0:
            return False
        i+=4
    return True


def divide(n):
    def rek(n,ile=0,dl=0,w=[],liczba=0):
        if n==0:
            if czy_pierwsza(ile+1) and czy_pierwsza(liczba):
                for i in w:
                    if not czy_pierwsza(i) and i!=0:
                        return False
                return True
            return False

        return rek(n//10,ile,dl+1,w,liczba+(n%10)*10**dl) or rek(n//10,ile+1,0,w+[liczba+(n%10)*10**dl],0)

    return rek(n)

print(divide(21722))