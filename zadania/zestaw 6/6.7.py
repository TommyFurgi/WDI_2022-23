def fun(m,T,i=0):
    if m==0:
        return True
    if i==len(T) or m<0:
        return False
    return fun(m-T[i],T,i+1) or fun(m,T,i+1)

T=[6,2,4,6]
print(fun(5,T))