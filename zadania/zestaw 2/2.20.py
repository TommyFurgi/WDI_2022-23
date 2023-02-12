def common_digit(x,y,s):
    D=[False]*s
    while x!=0:
        d=x%s
        D[d]=True
        x//=s
    while y!=0:
        if D[y%s]:
            return True
        y//=s
    return False
a,b = 123, 522
for s in range(2,17):
    if(common_digit(a,b,s)):
        continue
    else:
        print(s)
        break
else: 
    print("Nie ma ")