def climbing_stairs(n):
    if n<=1:
        return 1
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

n = int(input("Nhap so cau thang n: "))
print(f"So cach leo len bac {n} la: {climbing_stairs(n)}")