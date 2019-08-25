def accummulating_list(a):
    if a == []:
        return []
    x = [a[0]]
    a.pop(0)
    for char in a:
        x.append(x[-1] + char)
    return x
print(accummulating_list([1,2,3,4])) 
