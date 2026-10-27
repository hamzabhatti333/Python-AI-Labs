import random  


def play_game():
    # Choices list
    choices = ["rock", "paper", "scissors"]
    
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        # User input
        user_choice = input("Enter your choice (rock, paper, scissors) or type 'quit' to exit: ").lower()
        
        if user_choice == 'quit':
            print("Thanks for playing!")
            break
            
        if user_choice not in choices:
            print("Invalid choice! Please try again.")
            continue
            
        # Computer choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        # Winner decide karna
        if user_choice == computer_choice:
            print("It's a tie!\n")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!\n")
        else:
            print("You lose!\n")

# Game run karne ke liye
play_game()