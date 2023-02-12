def distance(T):
    n=len(T)
    row_max=0
    row_min=0
    for row in range(1,n):
        i=0
        while True:
            if T[row_max][i]==0 and T[row][i]==1:
                row_max=row
                break
            elif T[row_max][i]==1 and T[row][i]==0:
                break
            else:
                i+=1
        i=0
        while True:
            if T[row_min][i]==1 and T[row][i]==0:
                row_min=row
                break
            elif T[row_min][i]==0 and T[row][i]==1:
                break
            else:
                i+=1
    

    return abs(row_max-row_min)

T = [
    [1,0,0,0,1,1,1,0],
    [1,0,1,0,1,1,1,0],
    [0,0,0,0,1,1,1,0],
    [0,0,0,0,1,0,1,0],
    [1,0,0,0,1,1,1,1],
    [1,1,0,1,1,0,1,0],
    [1,0,0,0,0,0,1,0],
    [1,1,1,0,1,1,1,1]
]
print(distance(T))