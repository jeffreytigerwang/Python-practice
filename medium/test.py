n=7
m=3
dp = [[0] * n] * m
dp1 = [[0 for i in range(n)] for j in range(m)]


dp[2][6] = 3
dp1[2][6] = 3

print(dp)
print(dp1)




if dp == dp1:
    print('good')
else:
    print('bad')