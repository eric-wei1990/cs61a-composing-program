def divisions(n):
    return [1] + [x for x in range(2, n) if n % x == 0]

# print(divisions(20))

def perfect_number(n):
    return [x for x in range(1, n) if sum(divisions(x)) == x]

print(perfect_number(1000))