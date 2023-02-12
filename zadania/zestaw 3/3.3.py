def get_primes(n):
    A=[1]*(n+1)
    A[0]=0
    A[1]=0
    for el in range(2,n):
        if el==0:
            continue
        else:
            a=el*2
            while a<=n:
                print("zmienam ", a)
                A[a]=0
                a+=el
    return A
n=100
a = get_primes(n)
print(a)
for i in range(0,n):
    if a[i]==1:
        print(i)