def even_odd__transform(a,b):
    x = []
    for char in a:
        if char%2==0:
            char = char - (2*b)
        else:
            char = char + (2*b)
        x.append(char)
    return x
print(even_odd__transform([3,4,9], 3))
