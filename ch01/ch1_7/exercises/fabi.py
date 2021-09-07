def fabi(n):
    if n == 1:
        return 1
    else:
        return fabi(n-1) * n

def fab_iter(n):
    total = 1
    i = 1

    while (i <= n):
        total = total * i
        i = i + 1

    return total


print(fabi(4))
print(fab_iter(4))