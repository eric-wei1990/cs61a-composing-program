from operator import add

def apply_all(map_fn, list):
    return [map_fn(x) for x in list]

def map_fn(x):
    return x * 2

# print(apply_all(map_fn, [1, 2, 3]))

def filter(x):
    return x % 2 == 0

def keep_if(filter, list):
    return [x for x in list if filter(x)]

# print(keep_if(filter, [1, 2, 3, 4, 5]))

def reduce_fn(x, reducer):
    return x + reducer

def reduce(reduce_fn, list, initial = 1):
    reducer = initial

    for x in list:
        reducer = reduce_fn(x, reducer)

    return reducer

# print(reduce(reduce_fn, [1, 2, 3], 1))


def divisior_of(n):
    divisior_n = lambda x: n % x == 0
    return [1] + keep_if(divisior_n, range(2, n))


# print(divisior_of(6))

def sum_of_divisors(n):
    return reduce(add, divisior_of(n), 0)

# print(sum_of_divisors(6))

def perfect(n):
    return sum_of_divisors(n) == n

# print(perfect(6))
# print(perfect(10))

def get_perfect_numbers(n):
    return keep_if(perfect, range(1, n))

print(get_perfect_numbers(1000))