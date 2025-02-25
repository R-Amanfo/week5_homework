import random
#where I started
# def user_choice():
#     print("Hi, Welcome to the game. you may pick 3 options to play, R = Rock, S = Scissors or P = Paper\nThe answer must be one character")
#     input1 = input("What would you like to play/input: R(Rock), P(Paper), S(Scissors):")
#     accepted_input = "rps"
#     for letter in accepted_input:
#         if len(input1) > 1 or input1 not in letter.lower():
#             print("Error. Please enter a valid input:")
#             input1 = input("What would you like to play/input: R(Rock), P(Paper), S(Scissors): ")
#         else:
#             print(f"You have entered {input1}. Please wait for the computer to make a decision.")
#             break

def user_choice():
    print("Hi, Welcome to the game. You may pick 3 options to play, R = Rock, S = Scissors or P = Paper\nThe answer must be one character")
    user_input = input("What would you like to play/input: R(Rock), P(Paper), S(Scissors):")
    accepted_input = "RPS"
    converted_choice = {"R":"Rock", "P":"Paper", "S": "Scissors"}
    #used guide only for not in part of while loop for a little nudge, not the idea of a while loop
    while user_input.upper() not in accepted_input or len(user_input) > 1:
            print("Error. Please enter a valid input:")
            user_input = input("What would you like to play/input: R(Rock), P(Paper), S(Scissors): ")
    print(f"You have entered {converted_choice[user_input.upper()]}. Please wait for the computer to make a decision.")
    return converted_choice[user_input.upper()]

def computer_choice():
    computer_input = random.randint(0,2)
    possible_choice = ["Rock","Paper", "Scissors"]
    print(f"The computer has chosen {possible_choice[computer_input]}")
    return possible_choice[computer_input]


def main():
    user_choice()
    computer_choice()

#Tried to follow along with notes to implement main trick, however not getting desired output.

if __name__ == "__main__":
    main()









