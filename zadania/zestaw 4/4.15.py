def fun(t):
    n=len(t)
    i=0
    while i<n:
        j=0
        while j<n:
            l_copy=t[i][j]
            flaga=False
            while l_copy>0:
                if l_copy%10==2 or l_copy%10==3 or l_copy%10==5 or l_copy%10==7:
                    flaga=True
                l_copy//=10
            if flaga==False:
                break 
            if j==n-1:
                return True
            j+=1
        i+=1
    return False

t = [[2,2,1,7],
    [575,15,438,31],
    [9,8,7,88],
    [5,15,8,8]] 
print(fun(t))