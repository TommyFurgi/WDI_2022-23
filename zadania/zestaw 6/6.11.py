def rek(iloczyn,T):
    licznik=0
    def fun(iloczyn,T,i=0):
        if iloczyn==1:
            nonlocal licznik
            licznik+=1
            return    
        if i==len(T):
            return 
        
        fun(iloczyn,T,i+1)
        if iloczyn%T[i]==0:
            fun(iloczyn//T[i],T,i+1)

    fun(iloczyn,T)
    return licznik


T=[2,4,5,7,9,3,6]
print(rek(12,T))

'''
def fun(T,i,index,iloczyn=1):
    if i==1:
        return len(T[T==1])

    if iloczyn==i:
        return 1
    if index>=len(T):
        return fun(T,i,index+1,iloczyn*T[index])+fun(T,i,index+1,iloczyn)

'''