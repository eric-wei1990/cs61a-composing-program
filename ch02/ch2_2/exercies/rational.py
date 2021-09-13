from fractions import gcd

# def rational(n, d):
#     return [n, d]

def rational(n, d):
    g = gcd(n, d)
    print(g)
    return [n // g, d // g]

def numer(x):
    return x[0]

def denom(x):
    return x[1]

def add_rational(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rational(x, y):
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def print_rational(x):
    print(numer(x), '/', denom(x))

def rational_equal(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)

half = rational(1, 2)
print_rational(half)
third = rational(1, 3)
print_rational(mul_rational(half, third))
print_rational(add_rational(half, third))
print_rational(add_rational(third, third))