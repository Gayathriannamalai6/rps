import random
def determine_winner(user_play,computer_play):
    if user_play == computer_play:
        return("Opps!! It's a tie!!")
    elif user_play == 'rock':
        if computer_play == 'paper':
            return ("Opps! Computer is the winner!!")
        else:
            return ("Congrats! you are the winner!!")
    elif user_play == 'paper':
        if computer_play == 'scissors':
            return ("Opps! Computer is the winner!!")
        else:
            return ("Congrats! you are the winner!!")
    elif user_play == 'scissors':
        if computer_play == 'rock':
            return ("Opps! Computer is the winner!!")
        else:
            return ("Congrats! you are the winner!!")
    else:
        return("Invalid input.Please choose valid input")
def play_game():
    user_play =input("Enter your choice(rock? paper? or scissors?):")
    computer_play =random.choice(['rock','paper','scissors'])

    print("User's choice:",user_play)
    print("Computer's choice:",computer_play)
    print( determine_winner(user_play,computer_play ))
play_game()