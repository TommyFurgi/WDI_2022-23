def rek(t1,t2,suma=0,ile1=0,ile2=0,pos=0):
    if pos==len(t1):
        if suma==0 and ile1==ile2:
            return ile1
        return 0

    return max(rek(t1,t2,suma+t1[pos]-t2[pos],ile1+1,ile2+1,pos+1),rek(t1,t2,suma,ile1,ile2,pos+1),rek(t1,t2,suma+t1[pos],ile1+1,ile2,pos+1),rek(t1,t2,suma-t2[pos],ile1,ile2+1,pos+1)) 

t1=[2,4,3,8]
t2=[1,5,13,10]

print(rek(t1,t2))