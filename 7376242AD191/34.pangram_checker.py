def pangram(s):
    a = set("abcdefghijklmnopqrstuvwxyz")
    return a <= set(s.lower())

s = input()
print(pangram(s))
