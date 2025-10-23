def unique_paths_dp(m,n):
    dp = [[1] * n for _ in range(m)]
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]
m_dp, n_dp = 4,4
result_dp = unique_paths_dp(m_dp,n_dp)
print(f"So duong di duy nhat trong luoi: {m_dp}x{n_dp} la: {result_dp}")
