def left_rotations(a):
    y = [a]
    counter = 0
    while counter < len(a)-1:
        x = ''
        for char in range(len(a)):
            if a[char] == a[-1]:
                x += a[0]
            else:
                x += a[char+1]
        y.append(x)
        a = y[-1]
        counter += 1
    return y


print(left_rotations('abcdef'))

