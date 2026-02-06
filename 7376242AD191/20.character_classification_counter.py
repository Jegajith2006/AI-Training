def char_count(s):
    a = d = sp = 0
    for i in s:
        if i.isalpha():
            a += 1
        elif i.isdigit():
            d += 1
        else:
            sp += 1
    r = {"alphabets": a, "digits": d, "special": sp}
    return r

s = input()
print(char_count(s))

