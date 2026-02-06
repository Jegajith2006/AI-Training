def diag_sum(m):
    p = s = 0
    n = len(m)
    for i in range(n):
        p += m[i][i]
        s += m[i][n-i-1]
    return p, s

m = eval(input())
print(diag_sum(m))
