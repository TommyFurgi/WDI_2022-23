def fun(t):
    n=len(t)
    i=0
    while i<n:
        j=0
        flaga=False
        while j<n:
            l_copy=t[i][j]
            while l_copy>0:
                if l_copy%10==4 or l_copy%10==6 or l_copy%10==8 or l_copy%10==9 or l_copy%10==1 or l_copy%10==0:
                    break
                l_copy//=10
            if l_copy==0:
                flaga=True
                break
            j+=1
        if flaga==False:
            return False
        i+=1
    return True

t = [[2,22,1,7],
    [585,35,438,31],
    [9,8,7,88],
    [5,15,8,8]] 
print(fun(t))