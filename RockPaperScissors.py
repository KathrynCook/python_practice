import random

choices = ["rock", "paper", "scissors"]
play_again = "y"

print("Let's play Rock, Paper, Scissors! On the countdown, select your choice (rock, paper or scissors) to play! Type 'quit' if you would like to end the game.")
print("Ready?! \n3... \n2... \n1... \nGo! \n")

while play_again == "y":
    
    user_input = input("Pick rock, paper or scissors (or quit): ").lower()
    if user_input == "quit":
        print("Thanks for playing!")
        break
    if user_input not in choices:
        print("Hm, that's not a valid option...")
        continue

    random_number = random.randint(0,2)
    computer_pick = choices[random_number]

    print("The computer chose: " + computer_pick )

    if (user_input == "rock") and (computer_pick == "scissors"):
        print("You won!")
    elif (user_input == "paper") and (computer_pick == "rock"):
        print("You won!")
    elif (user_input == "scissors") and (computer_pick == "paper"):
        print("You won!")
    elif user_input == computer_pick:
        print("It's a draw!")
    else:
        print("You lost :(")

    play_again = input("Would you like to play again? (Y/N) ").lower()
    if play_again == "n":
        print("Thank you for playing, goodbye!")
        break
    elif (play_again != "y") and (play_again != "n"):
        print("Hm, not sure what you mean there... bye!")
        break