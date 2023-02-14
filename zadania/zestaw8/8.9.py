class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def usun_wezly(wsk,n):
    if wsk is None:
        return
    if n>1:
        tmp=wsk.right
        wsk.right=None
        usun_wezly(tmp,n-1)
        tmp=wsk.left
        wsk.left=None
        usun_wezly(tmp,n-1)    

a=Node(10)
b=Node(5,a)
c=Node(2)
e=Node(8)
d=Node(7,c,e)
f=Node(3,b)
g=Node(1,d,f)
usun_wezly(g,3)

print(b.left.val)
