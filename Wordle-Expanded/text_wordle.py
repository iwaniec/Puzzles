
board = ['[ ] [ ] [ ] [ ] [ ]',
         '[ ] [ ] [ ] [ ] [ ]',
         '[ ] [ ] [ ] [ ] [ ]',
         '[ ] [ ] [ ] [ ] [ ]',
         '[ ] [ ] [ ] [ ] [ ]',
         '[ ] [ ] [ ] [ ] [ ]']


letters = ['Q W E R T Y U I O P',
           ' A S D F G H J K L',
           '  Z X C V B N M']

word = 'PRIZE'

def update():
    print('\n-------------------')
    for row in range(len(board)):
        print(board[row])
    print('-------------------')
    for row in range(len(letters)):
        print(letters[row])
    print('-------------------\n')

update()

for row in range(6):

    print('Guess a 5-letter word:')
    guess = input()
    guess = guess[:5]
    guess = guess.upper()

    for i in range(5):

        if guess[i] == word[i]:
            new_row = board[row]
            pos = i*4+1
            new_row = new_row[:pos-1] + ' ' + word[i] + ' ' + new_row[pos+2:]
            board[row] = new_row

        elif guess[i] in word:
            new_row = board[row]
            pos = i*4+1
            new_row = new_row[:pos-1] + ' ' + guess[i].lower() + ' ' + new_row[pos+2:]
            board[row] = new_row

        else:
            for keys in range(3):
                letters[keys] = letters[keys].replace(guess[i], ' ')

    update()

    if guess == word:
        print('-------------------')
        print('Congrats! ', row+1, '/6', sep='')
        print('-------------------')
        break
