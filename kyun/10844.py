n = int(input())
dp = [[0 for x in range(10)] for y in range(n)]


for i in range(10):
    dp[0][i] = 1

for i in range(1, n):
    for j in range(0, 10):
        if j == 0:
            if i == 2:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j] + 1
        if j == 9:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
print(dp[n - 1])
sum = int(0)

for i in range(1, 10):
    sum = sum + dp[n - 1][i]

print(sum % 1000000000)
