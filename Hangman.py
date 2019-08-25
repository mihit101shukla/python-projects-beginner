import random
def hangman():

    def get_indices(a, b):
        x = []
        for tmp in range(len(a)):
            if a[tmp] == b:
             x.append(tmp)
        return x

    def pick_word():
        with open('sowpods.txt') as f:
            x = random.choice(f.readlines())
            f.close()
        return x.strip()


    counter = 0
    word = pick_word()
    print('\n' * 10)
    print('Welcome to Hangman!')
    print('For every correct guess a letter appears, else it states INCORRECT! ')
    print('You only have 6 incorrect attempts until game over')
    y = list('_' * len(word))
    print(' '.join(y))
    while '_' in y and counter < 6:
        w = input('Guess your letter: ').upper()
        if w not in word:
            counter += 1
            print(f'OOPS INCORRECT YOU HAVE {6 - counter} ATTEMPTS LEFT')
            if counter == 6:
                print('SORRY GAME OVER! ')
                print(f' Your word was {word}')
                if input('Would you like to play again, yes or no: ').lower() == 'yes':
                    hangman()
        else:
            for char in get_indices(word, w):
                y[char] = w
            print(' '.join(y))
        if '_' not in y:
            print('CONGRATULATIONS YOU WON!')
            if input('Would you like to play again, yes or no : ').lower() == 'yes':
                hangman()


hangman()