x = [2, 3, 1, 3, 4, 7, 4, 2, 8, 4, 2, 1, 7, 3]

con = 0


while con < len(x):
    x1 = x.count(x[con])
    if x1 > 1:
        x[con] = str(x[con]) * x1
    con += 1
print(set(x))
