n = int(input())
r = 0
for i in range(n+1):
    if (i%3 == 0) or (i%5 == 0):
        r += i
print(r)
