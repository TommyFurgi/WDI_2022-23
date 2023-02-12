n=int(input())
podstawa = int(input())
lista = [ "0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
wynik=""
while n>0:
    reszta = n%podstawa
    n//=podstawa
    wynik = lista[reszta]+wynik

print(wynik)

#z zajęć
def zamiana(liczba, system):
    znaki = ["0123456789ABCDEF"]
    wynik=""
    while liczba > 0:
        indeks=liczba%system
        wynik=znaki[indeks]+wynik
        liczba//=system
    print(znaki)
    return wynik
    
