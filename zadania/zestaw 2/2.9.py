def fun(k):
    eps = 1e-6
    x=1
    area = 0
    while x < k:
        area += 1/x *eps
        x+=eps
    return area