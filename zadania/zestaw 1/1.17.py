dzielenie2, dzielenie = 1, 0
a,b=1,1
while abs(dzielenie2-dzielenie):
    a,b=b,a+b
    dzielenie2 ,dzielenie=dzielenie, b/a
print(dzielenie)