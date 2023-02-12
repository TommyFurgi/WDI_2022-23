'''
Zadanie 3 (5 pkt)
Na szachownicy o wymiarach N na N wypełnionej liczbami naturalnymi > 1 odbywają się wyścigi
wież. Pierwsza wieża startuje z lewego górnego rogu i ma dotrzeć do prawego dolnego rogu szachownicy. Pierwsza wieża może wykonywać tylko ruchy w prawo lub w dół szachownicy. Druga wieża
startuje z prawego górnego rogu i ma dotrzeć do lewego dolnego rogu szachownicy. Druga wieża
może wykonywać tylko ruchy w lewo lub w dół szachownicy. Wygrywa wieża, która dotrze do mety
w mniejszej liczbie ruchów. Wieże mogą wykonać ruch z jednego pola na drugie tylko wtedy, gdy
liczby na obu polach są względnie pierwsze.
Proszę napisać funkcję, która dla danej tablicy zwraca numer wieży, która wygra wyścig lub 0, jeżeli
wyścig będzie nierozstrzygnięty. Można założyć, że podczas wyścigu wieże nie spotkają się na jednym
polu. Po wykonaniu funkcji zawartość tablicy nie może ulec zmianie.
'''
def nwd(a,b):
    while b:
        a,b=b,a%b
    return a

def fun(T):
    def rek1(T,x,y,a,b,ile=0,last=""):
        if x==a and y==b:
            return ile

        if last=="pion":
            return min(rek1(T,x,y+1,a,b,ile+1,last="poziom"),rek1(T,x+1,y,a,b,ile,last="pion"))
        elif last=="poziom":
            return min(rek1(T,x,y+1,a,b,ile,last="poziom"),rek1(T,x+1,y,a,b,ile+1,last="pion"))
        else:
            return min(rek1(T,x,y+1,a,b,ile+1,last="poziom"),rek1(T,x+1,y,a,b,ile+1,last="pion"))

    def rek2(T,x,y,a,b,ile=0,last=""):
        if x==a and y==b:
            return ile

        if last=="pion":
            return min(rek2(T,x,y-1,a,b,ile+1,last="poziom"),rek2(T,x+1,y,a,b,ile,last="pion"))
        elif last=="poziom":
            return min(rek2(T,x,y-1,a,b,ile,last="poziom"),rek2(T,x+1,y,a,b,ile+1,last="pion"))
        else:
            return min(rek2(T,x,y-1,a,b,ile+1,last="poziom"),rek2(T,x+1,y,a,b,ile+1,last="pion"))

    pierw=rek1(T,0,0,len(T)-1,len(T)-1)
    drug=rek2(T,0,len(T)-1,len(T)-1,0)
    if pierw==drug:
        return 0
    elif pierw>drug:
        return 2
    else:
        return 1