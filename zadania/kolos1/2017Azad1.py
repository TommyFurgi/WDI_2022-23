def fun(a,b):
    t=[False]*16
    for sys in range(2,17):
        a_copy=a
        while a_copy>0:
            t[a_copy%sys]=True
            a_copy//=sys
        b_copy=b
        while b_copy>0:
            if t[b_copy%sys]==True:
                break
            b_copy//=10
        else:
            return sys
        for i in range(1):
            t[i]=False
    return None
print(fun(123,522))