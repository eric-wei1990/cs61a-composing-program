def apply_all(map_fn, list):
    return [map_fn(x) for x in list]

def map_fn(x):
    return x * 2

print(apply_all(map_fn, [1, 2, 3]))

def filter(x):
    return x % 2 == 0

def keep_if(filter, list):
    return [x for x in list if filter(x)]

print(keep_if(filter, [1, 2, 3, 4, 5]))

def reduce_fn(x, reducer):
    return x + reducer

def reduce(reduce_fn, list, initial = 1):
    reducer = initial

    for x in list:
        reducer = reduce_fn(x, reducer)

    return reducer

print(reduce(reduce_fn, [1, 2, 3], 1))
