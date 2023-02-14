class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def ile_wezlow(wsk):
    if wsk is None:
        return 0
    if (wsk.right is not None and wsk.left is None) or (wsk.right is None and wsk.left is not None):
        return 1+ile_wezlow(wsk.left)+ile_wezlow(wsk.right)
    return ile_wezlow(wsk.left)+ile_wezlow(wsk.right)
    

a=Node(10)
b=Node(5,a)
c=Node(2)
e=Node(8)
d=Node(7,c,e)
f=Node(3,b)
g=Node(1,d,f)
print(ile_wezlow(g))