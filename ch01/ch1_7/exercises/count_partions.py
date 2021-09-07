def count_partions(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partions(n - m, m)
        without_m = count_partions(n, m - 1)
        return with_m + without_m

print(count_partions(2, 0))
print(count_partions(2, 1))
print(count_partions(3, 1))
print(count_partions(3, 2))
print(count_partions(6, 4))