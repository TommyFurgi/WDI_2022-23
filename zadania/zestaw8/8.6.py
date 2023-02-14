class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def ile_wezlow(wsk,n):
    if n<1:
        return 0
    if wsk is None:
        return 0
    elif n==1:
        return 1
    return ile_wezlow(wsk.right,n-1)+ile_wezlow(wsk.left,n-1)
    

a=Node(10)
b=Node(5,a)
c=Node(2)
e=Node(8)
d=Node(7,c,e)
f=Node(3,b)
g=Node(1,d,f)
print(ile_wezlow(g,3))