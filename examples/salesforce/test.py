alist = [0, 1, 0, 0]
blist = [0, 0, 1, 0]
# b[1] = 1
# res = [0, 1, 1, 0]

for i, (a, b) in enumerate(zip(alist, blist)):
    blist[i] = a or b

print(blist)
