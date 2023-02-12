'''1. Dana jest liczba naturalna N niezawierająca cyfry 0, którą rozbijamy na dwie liczby naturalne
A i B, przenosząc kolejne cyfry z liczby N do liczby A albo B. Na przykład liczbę 21523
możemy rozbić na wiele sposobów, np. (215,23),(2,1523),(223,15),(152,23),(22,153),(1,2523)...
Uwaga: względna kolejność cyfr w liczbie N oraz liczbach A i B musi być zachowana. Proszę
napisać funkcję generującą i wypisującą wszystkie rozbicia, w których powstałe liczby A i B
są względnie pierwsze. Do funkcji należy przekazać wartość N, funkcja powinna zwrócić liczbę
znalezionych par.
Uwagi:
- warunek względnej pierwszości można pominąć kosztem 1 pkt'''

def nwd(a,b):
    while b:
        a, b = b, a%b
    return a

def rek(N,A=0,B=0,posA=0,posB=0):
    if N==0:
        if nwd(A,B)==1 and A>=B:
            print(A,B)
        return

    return rek(N//10,A+(N%10)*10**posA,B,posA+1,posB) or rek(N//10,A,B+(N%10)*10**posB,posA,posB+1)

print(rek(21523))