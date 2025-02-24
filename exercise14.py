import random  # Import the random module to help the computer pick a random choice.


def get_user_choice():
    """Ask the user to choose Rock, Paper, or Scissors."""
    choices = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}  # Dictionary to match letters to full words.

    user_input = input(
        "Enter R for Rock, P for Paper, or S for Scissors: ").upper()  # Get user input and make it uppercase.

    if user_input in choices:  # Check if the input is valid.
        return choices[user_input]  # Return the full word (Rock, Paper, or Scissors).
    else:
        print("Invalid choice! Please enter R, P, or S.")  # Tell the user they entered something wrong.
        return get_user_choice()  # Ask again until they enter a valid choice.


def get_computer_choice():
    """Make the computer randomly pick Rock, Paper, or Scissors."""
    choices = ['Rock', 'Paper', 'Scissors']  # List of choices.
    return random.choice(choices)  # Randomly pick one from the list.


def determine_winner(user, computer):
    """Compare the choices and decide who wins."""
    if user == computer:  # If both choices are the same, it's a tie.
        return "It's a draw!"

    # Check all the ways the user can win.
    elif (user == "Rock" and computer == "Scissors") or \
            (user == "Paper" and computer == "Rock") or \
            (user == "Scissors" and computer == "Paper"):
        return "You win!"

    else:  # If the user didn't win and it's not a tie, they must have lost.
        return "You lose!"


def play_game():
    """Run the game step by step."""
    user_choice = get_user_choice()  # Get the user's choice.
    computer_choice = get_computer_choice()  # Get the computer's choice.

    # Show what both players picked.
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Decide and display the winner.
    result = determine_winner(user_choice, computer_choice)
    print(result)


# Start the game.
play_game()