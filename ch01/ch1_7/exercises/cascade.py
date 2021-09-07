def cascade(n):
    """Print a cascade of prefixes of n."""
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)

cascade(1234)