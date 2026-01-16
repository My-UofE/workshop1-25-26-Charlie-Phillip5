import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    x = (int)(len(poss_values)/2) + poss_values[0]
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    if (next_val > current_val) and (user_input == "h"):
        return True
    elif (next_val < current_val) and (user_input == "l"):
        return True
    return False

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    letter_in_word = False
    for i in range(len(word)):
        if word[i] == letter:
            board[i] = letter
            letter_in_word = True
    if letter_in_word:
        print("Well done! '"+letter+"' is in the word")
        return True
    else:
        print("Sorry, '"+letter+"' is not in the word")
        return False

