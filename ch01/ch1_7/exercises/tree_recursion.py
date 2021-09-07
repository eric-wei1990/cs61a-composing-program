def tree_recursion(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return tree_recursion(n - 2) + tree_recursion(n - 1)

print(tree_recursion(3))
print(tree_recursion(4))
print(tree_recursion(5))
print(tree_recursion(6))