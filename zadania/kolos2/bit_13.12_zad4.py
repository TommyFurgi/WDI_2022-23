def fun(t): 
    def rek(t,x=0,y=0,ruch=0):
        if x>len(t) or y>=len(t) or y<0 or t[x][y]==True:
            return float('inf')
        if x==len(t)-1:
            return ruch
        
        return min(rek(t,x+1,y+2,ruch+1),rek(t,x+1,y-2,ruch+1),rek(t,x+2,y+1,ruch+1),rek(t,x+2,y-1,ruch+1))

    ans=float('inf')
    for i in range(len(t)):
        ans=min(rek(t,0,i),ans)

    return ans