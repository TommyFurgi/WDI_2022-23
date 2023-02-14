class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def wstaw(wsk,n,last=None):#zakladam że drzewo nie jest puste
    if wsk is None:
        new=Node(n)
        if n<last.val:
            last.left=new
        else:
            last.right=new
        return
    if wsk.val==n:
        return
    elif wsk.val>n:
        wstaw(wsk.left,n,wsk)
    else:
        wstaw(wsk.right,n,wsk)

a=Node(13)
b=Node(14,a)
c=Node(10,None,b)
d=Node(4)
e=Node(7)
f=Node(6,d,e)
g=Node(1)
h=Node(3,g,f)
i=Node(8,h,c)
wstaw(i,11)