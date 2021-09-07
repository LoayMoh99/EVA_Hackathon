# Loay Mohamed
# Challeng 1:

s = input("Input string s:")
p = input("Input string p:")
res = True
index_s = 0
index_p = 0

while index_p < len(p) and index_s < len(s):
    if s[index_s] == p[index_p] or p[index_p] == '?':
        index_s += 1
        index_p += 1
    elif p[index_p] == '*':
        index_p += 1
        if index_p == 1:  # at the beginning
            index_s = index_p
        if index_p == len(p):  # at the end
            index_s = len(s)
    elif s[index_s] != p[index_p]:
        break
    else:
        index_s += 1

res = (index_p == len(p)) and (index_s == len(s))
# case if * is at the end and crossponds to epmty set
if index_s == len(s) and index_p == len(p)-1:
    if p[index_p] == '*':
        res = True
# case if empty s and p is only *
if len(s) == 0 and len(p) > 0:
    for char in p:
        if char != '*':
            res = False
            break
        res = True


print(res)
