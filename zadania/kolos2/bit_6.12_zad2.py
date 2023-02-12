def ile_sam(n):
    licz=0
    for i in n:
        if i=="a" or i=="e" or i=="o" or i=="u" or i=="y" or i=="i":
            licz+=1

    return licz


def suma_kod(n):
    s=0
    for i in n:
        s+=ord(i)
    return s

def wyraz(s1,s2,napis="",pos=0):
    if ile_sam(s1)==ile_sam(napis) and suma_kod(s1)==suma_kod(napis):
        print(napis)
        return True
    
    if pos>=len(s2):
        return False

    return wyraz(s1,s2,napis+s2[pos],pos+1) or wyraz(s1,s2,napis,pos+1)


print(wyraz("ula","pebxaey"))

    