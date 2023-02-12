def rek(T,k,pos=0,s1=0,s2=0,ile1=0,ile2=0):
    if pos==len(T):
        if ile1+ile2==k and s1==s2:
            return True
        return False

    return rek(T,k,pos+1,s1,s2,ile1,ile2) or rek(T,k,pos+1,s1+T[pos],s2,ile1+1,ile2) or rek(T,k,pos+1,s1,s2+T[pos],ile1,ile2+1)

T=[2,4,5,7,3,6]
print(rek(T,4))