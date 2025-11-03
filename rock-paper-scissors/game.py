import random

print("Welcome to Rock, Paper, Scissors!")

chooses = ['rock', 'paper', 'scissors']
def get_computer_choice():
    return random.choice(chooses)


player_score = 0
computer_score = 0

player_name = input("Enter your name: ")
print(f"Hello, {player_name}! Let's start the game.")

play =True

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return f"{player_name} wins!"
    else:
        return "Computer wins!"


def play_round():
    global player_score, computer_score
    player_choice = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower()
    if player_choice == 'quit':
        return False
    if player_choice not in chooses:
        print("Invalid choice. Please try again.")
        return True

    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(player_choice, computer_choice)
    print(result)

    if "wins" in result:
        if player_name in result:
            player_score += 1
        else:
            computer_score += 1

    print(f"Score - {player_name}: {player_score}, Computer: {computer_score}")
    return True

while play:
    play = play_round()
 
print(f"{player_name}: {player_score}, Computer: {computer_score}")


if play == False:
     if player_score > computer_score:
         print(f"Congratulations {player_name}, you won the game!")
     elif computer_score > player_score:
         print("Computer won the game! Better luck next time.")
     else:
        print("The game ended in a tie!")








