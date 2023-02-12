prev = 0
curr = 1
print(curr)
while curr+prev < 1000000:
        print(curr+prev)
        curr, prev = curr + prev, curr
