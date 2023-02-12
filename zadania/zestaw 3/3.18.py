def fun(tab):
    dl=len(tab)
    longest=0 #wartosc ktora zwaracmy
    for x in range(dl): #lewa strona, przesuwamy sie w prawo
        for y in range(x+1,dl): #lewa strona i przesuwamy sie w prawo
            flaga=True
            for i in range(y-x+1): #sprawdzamy czy w zakresie 
                if tab[x+i]!=tab[y-i] or tab[x+i]%2==0: # jezeli jest tutaj True to jest to zly ciag
                    flaga=False
                    break
            if flaga==True: #jak ciag okazal sie dobry to przypisz jego dlugosc to longest
                longest=max(longest,y-x+1)
    return longest

    
    
t=[2,1,3,7,3,1,5]
print(fun(t))