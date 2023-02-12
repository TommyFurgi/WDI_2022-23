'''Zadanie 2 (5 pkt)
Aby otrzymać nagrodę trzeba przejść kolejno przez N komnat. W każdej komnacie znajduje się
skrzynia (mogąca pomieścić maksymalnie 100 sztabek), w której umieszczono pewną liczbę sztabek
złota. Będąc w danej komnacie możemy zabrać ze skrzyni pewną liczbę sztabek albo dołożyć do
skrzyni wcześniej zebrane sztabki. Liczba sztabek przenoszona do następnej komnaty nie może
przekraczać 6. Drzwi do kolejnej komnaty otwierają się wtedy, gdy liczba sztabek pozostawiona
w skrzyni będzie liczbą pierwszą. Z ostatniej komnaty nie wolno wynieść żadnej sztabki. Proszę
napisać funkcję, która zwraca informację, czy jest możliwe przejście przez komanty. Do funkcji
należy przekazać tablicę zawierającą liczby sztabek w kolejnych komnatach. Na przykład:
T = [10, 20, 30] −→ funkcja powinna zwrócić False
T = [10, 20, 35] −→ funkcja powinna zwrócić True, w komnatach pozostanie [5, 23, 37]'''
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

def rek(T,pos=0,ile_mam=0):
    if pos==len(T):
        if ile_mam==0:
            return True
        return False

    for i in range(-6,7): # i - tyle zabieram
        if 0<=ile_mam+i<7 and T[pos]-i<=100 and czy_pierwsza(T[pos]-i) and i<=T[pos]:
            if rek(T,pos+1,ile_mam+i):
                return True
    return False

print(rek([10, 20, 35]))