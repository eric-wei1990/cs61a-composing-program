def is_even(n):
    print(n)
    if n == 0:
        return True
    else:
        return is_odd(n - 1)

def is_odd(n):
    print(n)
    if n == 0:
        return False
    else:
        return is_even(n - 1)

print(is_even(3))
print(is_even(4))
print(is_odd(3))
print(is_odd(4))