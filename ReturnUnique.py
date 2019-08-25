def returnUnique(a):
    x = []
    for char in a:
        if a.count(char) == 1:
            x.append(char)
    return x
print(returnUnique([5,5,2,4,4,4,9,9,9,1]))