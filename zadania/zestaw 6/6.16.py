def wyraz(s1,s2,wynik="",indeks=0):
    if len(s1)>len(s2):
        return False
    if indeks==len(s2):
        if czy_mozna(s1,wynik):
            print(wynik)
            return True
        else:
            return False
    return wyraz(s1,s2,wynik,indeks+1) or wyraz(s1,s2,wynik+s2[indeks],indeks+1)

def czy_mozna(s1,wynik):
    licznik=0
    asci=0
    for i in range(len(s1)):
        asci+=ord(s1[i])
        if ord(s1[i])==97 or ord(s1[i])==101 or ord(s1[i])==105 or ord(s1[i])==111 or ord(s1[i])==117 or ord(s1[i])==121:
            licznik+=1

    for i in range(len(wynik)):
        asci-=ord(wynik[i])
        if ord(wynik[i])==97 or ord(wynik[i])==101 or ord(wynik[i])==105 or ord(wynik[i])==111 or ord(wynik[i])==117 or ord(wynik[i])==121:
            licznik-=1

    if asci==0 and licznik==0:
        return True


print(wyraz("ula","ketxey"))