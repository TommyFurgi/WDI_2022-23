def fun(n):
    row, col = 0, 0
    tab=[[0 for _ in range(n)] for _ in range(n)]
    p=1
    while p <= n**2:
        for i in range(col,n-col):
            tab[row][i]=p
            p+=1
        for i in range(row+1,n-row):
            tab[i][n-col-1]=p
            p+=1
        for i in range(n-col-2,col-1,-1):
            tab[n-row-1][i]=p
            p+=1
        for i in range(n-row-2,row,-1):
            tab[i][col]=p
            p+=1


        col+=1
        row+=1
    return tab



for i in fun(5):
    print(i)
