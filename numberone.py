def sum_squares(*angka) :
    listNumber = [*angka]
    ss = 0
    for num in listNumber:
        ss += num**2
    return ss

print(sum_squares(1, 2, 3))