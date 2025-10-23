import sys
def matrix_chain_multiplication(p: list[int]) -> int:
    n = len(p) - 1
    m = [[0] * (n+1) for _ in range(n+1)]
    for l in range(2, n+1):
        for i in range(1, n-l+2):
            j = i + l - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                cost = m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j]
                if cost < m[i][j]:
                    m[i][j] = cost
    return m[1][n]

p_example = [30, 35, 15, 5]
result_min_multiplications = matrix_chain_multiplication(p_example)
print(f"Kich thuoc: {p_example}")
print(f"So phep nhan toi thieu: {result_min_multiplications}")