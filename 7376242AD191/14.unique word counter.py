def count_word(s):
    r = set(s.lower().split())
    return len(r)

s = input()
print(count_word(s))
