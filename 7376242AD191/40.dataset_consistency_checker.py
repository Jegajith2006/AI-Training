def check_data(d):
    k = d[0].keys()
    for i in d:
        if i.keys() != k:
            return "Inconsistent"
    return "Consistent"

d = eval(input())
print(check_data(d))
