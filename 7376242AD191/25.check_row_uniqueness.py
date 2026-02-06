def row_unique(m):
    for r in m:
        if len(r) != len(set(r)):
            return False
    return True

m = eval(input())
print(row_unique(m))

