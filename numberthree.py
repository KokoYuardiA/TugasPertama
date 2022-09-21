def pangkat(x, y):
    temp = x
    if x < 0 or y < 0:
        return "only accept positive number"
    if y == 0:
        return 1
    counter = 0
    while counter < y - 1:
        x = x * temp
        counter += 1
    return x

print(pangkat(3, 2))