import random

def hangman ():
    word_list=['python','random','import','kotlin','java']
    random_number=random.randint(0,4)
    word=word_list[random_number]
    wrong=0
    stages=['',
            '_________        ',
            '|        |       ',
            '|        |       ',
            '|        0       ',
            '|       /|\      ',
            '|       / \      ',
            '|                '
            ]
    rletters=list(word)
    board=['__'] * len(word)
    win=False
    print('Добро пожаловать на казнь!')
    while wrong < len(stages) -1:
        print('\n')
        msg='Введите букву:'
        char= input(msg)
        if char in rletters:
            cind=rletters.index(char)
            board[cind]=char
            rletters[cind]= '$'
        else:
            wrong += 1
        print((' '.join(board)))
        e=wrong+1
        print('\n'.join(stages[0:e]))
        if '__' not in board:
            print('Вы выйграли! Было загадано слово: ')
            print(' '.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0: wrong]))
        print('Вы проиграли! Было загадано слово:{}.'.format(word))
hangman ()
            
    
