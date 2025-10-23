def knapsack_01_dp(W, weights, values, n):
    K = [[0 for w in range(W+1)] for i in range(n+1)]
    for i in range(1, n+1):
        for w in range(W+1):
            current_weight = weights[i-1]
            current_value = values[i-1]
            if current_weight > w:
                K[i][w] = K[i-1][w]
            else:
                val_not_include = K[i-1][w]
                val_include = current_value + K[i-1][w - current_weight]
                K[i][w] = max(val_not_include, val_include)
    return K[n][w], K
if __name__ == '__main__':
    W = 7
    weights = [2,3,4]
    values = [3,4,5]
    n = len(values)

    max_value, dp_table = knapsack_01_dp(W,weights,values,n)

    print(f"Suc chua toi da (W): {W}")
    print(f"Khoi luong cac vat pham: {weights}")
    print(f"Gia tri vat pham: {values}")
    print("\n---Bang Quy hoach tu dong (DP Table) ---")
    
    print(" w: 0 1 2 3 4 5 ...")
    for i, row in enumerate(dp_table):
        if i == 0:
            print(f"i=0: {row[:51]}")
        else:
            print(f"i={i}: {row[:51]}")
    print("\n------------------------------")
    print(f"Gia tri toi da co the dat duoc: {max_value}")
