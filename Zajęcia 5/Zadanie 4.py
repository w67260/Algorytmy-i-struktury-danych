def wspolczynnik(n, m):
    W = [[0 for j in range(m+1)] for i in range(n+1)]

    for i in range(n+1):
        for j in range(min(i, m)+1):
            if j == 0 or j == i:
                W[i][j] = 1
            else:
                W[i][j] = W[i-1][j] + W[i-1][j-1]

    return W[n][m]