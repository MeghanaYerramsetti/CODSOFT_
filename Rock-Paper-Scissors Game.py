import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def main():
    print("Welcome to Rock-Paper-Scissors!")
    
    user_score = 0
    computer_score = 0
    
    while True:
        user_choice = input("\nChoose rock, paper, or scissors (or 'q' to quit): ").lower()
        
        if user_choice == 'q':
            print("Thanks for playing! Final Score - You: {}, Computer: {}".format(user_score, computer_score))
            break
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}")

        play_again = input("Would you like to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Final Score - You: {}, Computer: {}".format(user_score, computer_score))
            break

if __name__ == "__main__":
    main()
