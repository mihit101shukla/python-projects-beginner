def num_of_sublists(a):
    if type(a[0]) != list:
        return 0
    return len(a)
print(num_of_sublists([[1, 2, 3], [1,2,3]]))