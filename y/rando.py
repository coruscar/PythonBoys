from random import randint

player = input('rock (r), paper (p) or scissors? Or press q to end the game. ')
# player = input('要出石头(r), 剪刀(s) 还是布(p)？')

# Play the game continuously.
while player != 'q':
    
    if player == 'r':
        player = 'rock'
        # player = '石头'

    elif player == 's':
        player = 'scissors'
        # player = '剪刀'

    else:
        player = 'paper'
        # player = '布'

    # random number gen.
    chosen = randint(1,3)

    # conditions.
    if chosen == 1:
        computer = 'rock'
        # computer = '石头'

    elif chosen == 2:
        computer = 'scissors'
        # computer = '剪刀'

    else:
        computer = 'paper'
        # computer = '布'

    # End with a white space instead of new line.
    print('Player: ', player, 'vs', 'Computer: ', computer)
    # print("玩家出了", cplayer, "，", "电脑出了", computer, "。")

    if player == computer:
        print('DRAW! ')
        # print('平局！')

    elif ((player == 'rock' and computer == 'scissors') or (player == 'scissors' and computer == 'paper') or (player == 'paper' and computer == 'rock')):
        print('Player wins! ')
        # print('玩家赢了！')
    else:
        print('Computer wins! ')
        # print('电脑赢了！')

    player = input('rock (r), paper (p) or scissors? Or press q to end the game. ')

##### Okay I got the above to work. Will come back to see if I can make a Chinese ver. LOL.
