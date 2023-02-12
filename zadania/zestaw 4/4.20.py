def suma(board,x1,x2,y1,y2,row,col):
    if x1==x2:
        return row[x1]+col[y1]+col[y1] -board[x1][y1]-board[x2][y2]
    if y1==y2:
        return col[y1]+row[x1]+row[x2] -board[x1][y1]-board[x2][y2]
    
    return row[x1]+row[x2]+col[y1]+col[y2] -board[x1][y1]*2-board[x2][y2]*2-board[x2][y1]-board[x1][y2]


def fun(board):
    n=len(board)
    row=[0]*n
    col=[0]*n
    for x in range(n):
        suma=0
        for y in range(n):
            suma+=board[x][y]
        row[x]=suma
    for y in range(n):
        suma=0
        for x in range(n):
            suma+=board[x][y]
        col[y]=suma
    suma_najw=0
    for x1 in range(n):
        for y1 in range(n):
            for x2 in range(n):
                for y2 in range(n):
                    if x1==x2 and y1==y2:
                        continue
                    if suma(board,x1,x2,y1,y2,row,col)>suma_najw:
                        best=(x1,y1,x2,y2)
                        suma_najw=suma(board,x1,x2,y1,y2,row,col)
    return best
