import random
c = 0
d = 0
while c < 3 and d < 3:
    a = input('Enter your choice: Rock, Paper or Scissors ')
    b = random.randint(1, 3)
    if a == 'rock' and b == 3:
        print('Player 1 won!')
        c = c + 1
    elif a == 'rock' and b == 2:
        print('Player 2 won!')
        d = d + 1
    elif a == 'rock' and b == 1:
        print('Tie!')
    elif a == 'paper' and b == 1:
        print('Player 1 won!')
        c = c + 1
    elif a == 'paper' and b == 3:
        print('Player 2 won!')
        d = d + 1
    elif a == 'paper' and b == 2:
        print('Tie!')
    elif a == 'scissors' and b == 1:
        print('Player 2 won!')
        d = d + 1
    elif a == 'scissors' and b == 2:
        print('Player 1 won!')
        c = c + 1
    else:
        print('Tie!')
if c == 3:
    print('You got three points! Game over!')
else:
    print('The computer got three points! Game over!')
