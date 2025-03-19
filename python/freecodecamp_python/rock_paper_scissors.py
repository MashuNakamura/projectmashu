import random

def play():
    player = input("'r' for rock, 'p' for paper, 's' for scissors : ")
    computer = random.choice(['r', 'p', 's'])
    print(computer)

    if player == computer:
        return 'Tie'

    if win:
        return 'You Win'
    
    return 'You Lose'

def win(human, opponent):
    if (human == 'r' and opponent == 's') or (human == 'p' and opponent == 'r') or (human == 's' and opponent == 'p'):
        return True

print(play())
