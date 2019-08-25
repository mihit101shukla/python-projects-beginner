def anagrams(a):
    x = []
    with open('sowpods.txt') as f:
        for char in f:
            if char.strip().lower() in a:
                x.append(char.strip().lower())
    return x

print(anagrams('bob'))