def concat(*args):
    x = []
    for char in args:
        x += char
    return x
print(concat([1,2,3], [4,5], [6,7]))