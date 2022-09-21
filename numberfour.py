from operator import truediv


def palindorome(kata):
    if kata == kata[::-1]:
        return True
    else:
        return False

print(palindorome("rotator"))