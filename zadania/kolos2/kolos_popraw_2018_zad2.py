'''Dane s¡ dwie tablice int t1[N] oraz int t2[N] wypeªnione liczbami naturalnymi. Elementy z tablic t1 i t2
ª¡czymy w pary (po jednym elemencie z ka»dej tablicy) tak, aby suma wybranych elementów z tablicy t1 byªa
równa sumie wybranych elementów z tablicy t2. Prosz¦ napisa¢ funkcj¦, która zwróci maksymaln¡ liczb¦
par, jak¡ mo»na uzyska¢. Do funkcji nale»y przekaza¢ wyª¡cznie tablice t1 i t2, funkcja powinna zwróci¢
maksymaln¡ liczb¦ par.'''


def rek(t1,t2,suma,l1,l2,pos=0):
    if pos==len(t1):
        if suma==0 and l1==l2 and l1!=0:
            return l1
        return 0

    
    return max(rek(t1,t2,suma,l1,l2,pos+1),rek(t1,t2,suma+t1[pos],l1+1,l2,pos+1),rek(t1,t2,suma-t2[pos],l1,l2+1,pos+1),rek(t1,t2,suma+t1[pos]-t2[pos],l1+1,l2+1,pos+1))

