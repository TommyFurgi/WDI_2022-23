a, b = 0, 100
while abs(a-b) > 0.0000001:
    polowa = (a+b)/2
    if polowa**2 - 2020 == 0:
        break
    if (a**2-2020)*(polowa**2-2020) < 0:
        b=polowa
    elif (b**2-2020)*(polowa**2-2020) < 0:
        a = polowa
print(polowa)