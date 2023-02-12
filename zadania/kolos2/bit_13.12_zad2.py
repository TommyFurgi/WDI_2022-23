def rek(t,x=0,y=0,suma=0):
    if x==len(t)-1 and y==len(t)-1:
        return suma
    if x>=len(t) or y>=len(t):
        return float('inf')
    
    return min(rek(t,x+1,y,suma+t[x][y]),rek(t,x,y+1,suma+t[x][y]))

t=[
    [0,5,4,3],
    [2,1,3,2],
    [8,2,5,1],
    [4,3,2,0],
]
print(rek(t))