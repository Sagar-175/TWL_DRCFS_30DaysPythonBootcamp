# Rock paper scissors
import random
print("Welcome!!! Let's play a game")
options = ['rock', 'paper', 'scissors']
print(options)
player2 = random.choice(options)
print(player2)
for i in range(5):
    player1 = input("Choose your answer:")
    if player1 == player2:
        print('The game is tie. No one wins')
    elif player1 == 'rock' and player2 == 'scissors':
        print('Player 1 wins')
    elif player1 == 'rock' and player2 == 'paper':
        print('Player 2 wins')
    elif player1 == 'paper' and player2 == 'rock':
        print('Player 1 wins')
    elif player1 == 'paper' and player2 == 'scissors':
        print('Player 2 wins')
    elif player1 == 'scissors' and player2 == 'paper':
        print('Player 1 wins')
    elif player1 == 'scissors' and player2 == 'rock':
        print('Player 2 wins')