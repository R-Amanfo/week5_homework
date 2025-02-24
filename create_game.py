import random

# prompts the user to enter a value R, P, S
# the program should convert this value into Rock, Paper, Scissors respectively
# Asks the computer to generate a random value between 0 and 2
# convert the computers choice. 0 becomes Rock, 1 becomes Paper, 2 becomes scissors
# compare the user's choice with the computers choice to display a message indicating whether
# the user won, lost or drew against the computer
# don't use print function
# do not use lambda or nested functions
# do not use global variables
# use main trick


# prompts the user to enter a value 0,1,2
# 0: Rock 1: Paper 2: Scissors,
# function play defined to store block of code which will be executed
# variables choice and user input added to convert the users choice into the values
# choice dictionary uses integers (0-2) as keys and their values 'Rock' 'Paper' 'Scissors'
# in Python dictionaries use key value pairs
# import random (module) to generate computers random choice using random.randint(0,2)
# and then convert the random integer into string value
# function select_winner (meaningful name)added to store conditional statements
# if elif and else
def play():
        """
        this function stores block of code that will prompt the users choice
        use of imported random module
        and also include random.randit for selecting computer's choice
        and if incorrect value is entered - not valid a choice
        :return:
        """
        choice = {0: 'Rock', 1: 'Paper', 2: 'Scissors'}
        user_input = input('Enter your choice (Type 0 for Rock, 1 for Paper, 2 for Scissors):')

        if user_input not in ['0', '1', '2']:
            return "Not a valid choice. Try again"

        user_choice = {'0': 'Rock', '1': 'Paper', '2': 'Scissors'}[user_input]
        computer_choice = choice[random.randint(0, 2)]

        result = select_winner(user_choice, computer_choice)
        return f'You selected {user_choice}. Computer selected {computer_choice}. {result}'

def select_winner(user, computer):
        """
        this function determines who is the winner
        compares the user and computer input
        use of conditional statements
        :param user:
        :param computer:
        :return:
        """
        if user == computer:
            return "You drew!"
        elif (user == 'Rock' and computer == 'Scissors') or \
                (user == 'Paper' and computer == 'Rock') or \
                (user == 'Scissors' and computer == 'Paper'):
            return "You won!"
        else:
            return "You lost!"


# main trick in Python
# the block of code is only run when the script is run directly and not imported as a module
#
if __name__ =='__main__':
    result_message = play()
    print(result_message)
