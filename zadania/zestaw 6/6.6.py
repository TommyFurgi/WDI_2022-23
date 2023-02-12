def fun(T,i=0,sum=0,sum_id=0,licz=0):

    if i==len(T):
        if sum_id==sum and sum!=0:
            return licz
        else:
            return float('inf')

    return min(fun(T,i+1,sum,sum_id,licz),fun(T,i+1,sum+T[i],sum_id+i,licz+1))

T= [1,7,3,5,2]
print(fun(T))