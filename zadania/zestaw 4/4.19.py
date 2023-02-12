import math
def fun(t,iloczyn):
    n=len(t)
    i=0
    licznik=0
    while i<n:
        j=0
        while j<n:
            if t[i][j]<=math.sqrt(iloczyn):
                for x1,y1 in [(i-1, j-2),(i+1, j-2),(i-2, j-1),(i-2, j+1),(i-1, j+2),(i+1, j+2),(i+2, j-1),(i+2,j-2)]:
                    if x1<0 or x1>=n or y1<0 or y1>=n:
                        continue
                    
                    if iloczyn==t[i][j]*t[x1][y1]:
                        licznik+=1

                    '''
                    if i>0 and j>1:
                    if iloczyn==t[i][j]*t[i-1][j-2]:
                        licznik+=1
                if i+1<n and j>1:
                    if iloczyn==t[i][j]*t[i+1][j-2]:
                        licznik+=1
                if i>1 and j>0:
                    if iloczyn==t[i][j]*t[i-2][j-1]:
                        licznik+=1
                if i>1 and j+1<n:
                    if iloczyn==t[i][j]*t[i-2][j+1]:
                        licznik+=1
                if i>0 and j+2<n:
                    if iloczyn==t[i][j]*t[i-1][j+2]:
                        licznik+=1
                if i+1<n and j+2<n:
                    if iloczyn==t[i][j]*t[i+1][j+2]:
                        licznik+=1
                if i+2<n and j>0:
                    if iloczyn==t[i][j]*t[i+2][j-1]:
                        licznik+=1
                if i+2<n and j>1:
                    if iloczyn==t[i][j]*t[i+2][j-2]:
                        licznik+=1
                '''
            j+=1
        i+=1
    return licznik

t = [[2,22,1,7],
    [585,35,438,31],
    [9,8,7,88],
    [5,15,8,8]] 
print(fun(t,35))