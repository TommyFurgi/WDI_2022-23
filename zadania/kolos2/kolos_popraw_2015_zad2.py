'''zad-wdi kolokwium 2, piątek,5lutego 2016 
Zad. 2 Dana jest N elementowy zbiór liczb naturalnych w postaci tablicy int t[N]. Proszę napisać
funkcję, która zwraca informację czy jest możliwy podział zbioru na trzy zbiory tak aby w każdym z
trzech zbiorów lączna liczba jedynek w liczbach zapisanych w systemie binarnym była jednakowa. Na
przykład dla zbioru [2,3,5,7,11,13,16] możliwy podział to {2,13,16} {3,11} {5,7} czyli w systemie
dwójkowym {10,1101,10000} {11,1011} {101,111} - w każdym zbiorze jest 5 jedynek.
'''

def zad(t):
    tab=[0]*len(t)
    for i in range(len(t)):
        suma=0
        l_copy=t[i]
        while l_copy>0:
            suma+=l_copy%2
            l_copy//=2
        tab[i]=suma
    
    def rek(tab,pos=0,s1=0,s2=0,s3=0):
        if pos==len(tab):
            if s1==s2 and s1==s3:
                return True
            return False

        return rek(tab,pos+1,s1+tab[pos],s2,s3) or rek(tab,pos+1,s1,s2+tab[pos],s3) or rek(tab,pos+1,s1,s2,s3+tab[pos])

    return rek(tab)
    
t=[2,3,5,7,11,13,16]
print(zad(t))