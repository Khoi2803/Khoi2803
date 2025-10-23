def quan_ly_dau_tu(M, costs, profits):
    n = len(costs)
    DP = [[0 for c in range(M+1)] for i in range(n+1)]
    for i in range(1, n+1):
        for c in range(M+1):
            cost_i = costs[i-1]
            profit_i = profits[i-1]
            if cost_i >c:
                DP[i][c] = DP[i-1][c]
            else:
                profit_not_include = DP[i-1][c]
                profit_include = profit_i + DP[i-1][c - cost_i]
                DP[i][c] = max(profit_not_include,profit_include)
    max_profit = DP[n][M]
    projects_chosen = []
    c = M
    for i in range(n, 0, -1):
        if DP[i][c] != DP[i-1][c]:
            project_index = i
            projects_chosen.append((project_index, profits[i-1], costs[i-1]))
            c -= costs[i-1]
    projects_chosen.reverse()

    return max_profit, projects_chosen, DP
if __name__ == '__main__':
    M = 10
    costs = [5,4,3]
    profits = [12,8,5]
    max_profit, projects_chosen, dp_table = quan_ly_dau_tu(M, costs, profits)
    
    print(f"Tổng Vốn Đầu Tư (M): {M}")
    print(f"Danh sách Dự án (Chi phí, Lợi nhuận): {list(zip(costs, profits))}")
    print("\n-------------------------------------")
    print(f"Lợi nhuận tối đa có thể đạt được: {max_profit}")
    
    print("\nCác dự án đã chọn:")
    total_cost = 0
    total_profit = 0
    for index, profit, cost in projects_chosen:
        print(f"  - Dự án {index} (Chi phí: {cost}, Lợi nhuận: {profit})")
        total_cost += cost
        total_profit += profit
        
    print(f"\nKiểm tra: Tổng Chi phí đã đầu tư: {total_cost} (<= {M})")
    print(f"Kiểm tra: Tổng Lợi nhuận: {total_profit}")

    print("\n--- Bảng Quy hoạch động (DP Table) ---")
    header = "i/c | " + " | ".join([f"{c:2}" for c in range(M + 1)])
    print(header)
    print("-" * (len(header) + 2))
    
    for i, row in enumerate(dp_table):
        row_str = " | ".join([f"{val:2}" for val in row])
        print(f"{i:3} | {row_str}")