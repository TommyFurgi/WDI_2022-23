def rek(t,suma1=0,suma2=0,ile1=0,ile2=0,pos=0):
    if pos==len(t):
        if suma1==suma2 and ile1==ile2 and ile1!=0:
            return True
        return False

    return rek(t,suma1+t[pos],suma2,ile1+1,ile2,pos+1) or rek(t,suma1,suma2+t[pos],ile1,ile2+1,pos+1) or rek(t,suma1,suma2,ile1,ile2,pos+1)

t=[1,5,2,3,4,7]
print(rek(t))
