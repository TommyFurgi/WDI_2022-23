class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def wypisz(wsk):
    if wsk is not None:
        print(wsk.val)
        wypisz(wsk.right)
        wypisz(wsk.left)


