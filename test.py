def even_nums():
    res = []
    for i in range(1, 51):
        if i % 2 == 0:
            res.append(i)
    return res

print(even_nums())
