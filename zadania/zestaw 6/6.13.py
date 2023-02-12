def fun(l,W=[],i=1):
    if l<0:
        return
    elif l==0:
        if len(W)<2:
            return
        print(W)
        return
    elif i>l:
        return

    fun(l-i,W+[i],i)
    fun(l,W,i+1)

fun(4)
