def fun(m,T):
    
    def rek(m,T,i=0,W1=[],W2=[],b=False):

        if m==0 and b==False:
            b=True
            print(W1,W2)
        if i!=len(T):
            rek(m,T,i+1,W1,W2,b) 
            rek(m-T[i],T,i+1,W1+[T[i]],W2,b=False) 
            rek(m+T[i],T,i+1,W1,W2+[T[i]],b=False)
    rek(5,T)
T=[2,4,7,3]
fun(5,T)