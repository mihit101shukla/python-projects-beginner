def quad_solutions(a,b,c):
    if (b*b) - 4*(a*c) > 0:
        return 2
    if (b*b) - 4*(a*c) == 0:
        return 1
    else:
        return 0
print(quad_solutions(1,0,1))