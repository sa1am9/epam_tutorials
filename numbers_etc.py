s = [1,1,1,1,1,1,1,1,1, 10]

weight = 11

s.sort()
sum = 0
i = 0
while sum < weight:
    sum += s[i]
    i += 1
sum -= s[i-1]
print(sum)

