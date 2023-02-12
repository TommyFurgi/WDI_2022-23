def rek(iloczyn,ile,T):
    licznik=0
    def fun(iloczyn,ile,T,i=0,W=[]):
        if iloczyn==1 and ile==0:
            nonlocal licznik
            licznik+=1
            print(W)
            return    
        if i==len(T):
            return 
        
        fun(iloczyn,ile,T,i+1,W)
        if iloczyn%T[i]==0:
            fun(iloczyn//T[i],ile-1,T,i+1,W+[T[i]])

    fun(iloczyn,ile,T)
    return licznik


T=[2,4,5,7,1,3,12]
print(rek(12,2,T))