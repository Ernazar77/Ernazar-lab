import random

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif user_choice == 1 and computer_choice == 2:
        return "User"
    elif user_choice == 2 and computer_choice == 3:
        return "User"
    elif user_choice == 3 and computer_choice == 1:
        return "User"
    else:
        return "Computer"

def main():
    user_choice = input("Enter your choice (rock, scissors, paper): ")
    if user_choice == "rock":
        user_choice = 1
    elif user_choice == "scissors":
        user_choice = 2
    elif user_choice == "paper":
        user_choice = 3
    else:
        print("Invalid choice. Please choose rock, scissors, or paper.")
        return

    computer_choice = get_computer_choice()

    print("Computer's choice:")
    if computer_choice == 1:
        print("rock")
    elif computer_choice == 2:
        print("scissors")
    else:
        print("paper")

    winner = determine_winner(user_choice, computer_choice)

    if winner == "Tie":
        print("It's a tie!")
    else:
        print(f"{winner} wins!")

if __name__ == "__main__":
    main()