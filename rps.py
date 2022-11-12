# library needed in this 
import random

def play():
    user = input("R for Rock, P for Paper and S for Scissors\nSelect your choice: ").lower()
    computer = random.choice(['r','p','s'])
    if user == computer:
        return "It's a Tie"
    
    elif is_win(user,computer):
        return "You Win!"
    
    return "You Lose!"    
    # r>s,s>p,p>r
def is_win(player,oppenent):
    # return true if player wins 
    # r>s,s>p,p>r
    if ((player == 'r'and oppenent=='s') or (player == 's'and oppenent=='p') or (player == 'p'and oppenent=='r')):
        return True
    
    
print(play())