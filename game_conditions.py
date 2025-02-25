# import game_functions
from game_functions import user_choice, computer_choice
user_input =  user_choice()
computer_input = computer_choice()


#Tried to use conditional while importing functions from game_functions file. Doesn't seem to work as intended. Not quite sure what I'm doing wrong.
# print(user_choice())
# print(computer_choice())

if user_input == computer_input:
    print("It's a tie")
elif user_input == "Rock" and computer_input == "Scissors":
    print("Yow win!")
elif user_input == "Scissors" and computer_input == "Paper":
    print("You win!")
elif user_input == "Paper" and computer_input == "Rock":
    print("You win!")
else:
    print("Computer wins")
