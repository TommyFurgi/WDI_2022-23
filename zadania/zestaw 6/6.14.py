def fun(n,z,do,uzyj):
    if n==1:
        print(z," -> ",do)
        return
    
    fun(n-1,z,uzyj,do)
    print(z," -> ",do)
    fun(n-1,uzyj,do,z)
    
fun(3,"A","B","C")