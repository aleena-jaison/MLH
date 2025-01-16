# Rock Paper Scissors Game
import random

choices = ['rock','paper','scissors']
user_score = 0
computer_score = 0
rounds = int(input("Enter the number of rounds you want to play: "))
for i in range(rounds):
    user_choice=input("\nEnter your choice (rock, paper, scissors): ").lower()
    if user_choice not in choices:
        print("Invalid choice! Please enter correct choice (rock, paper, scissors)")
        continue
    computer_choice=random.choice(choices)
    print(f"\n2Computer's choice: {computer_choice}")
    print(f"Your choice: {user_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock'and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1
    print(f"Current scores - You: {user_score}, Computer: {computer_score}")

print("\nGame Over!")
print(f"\nFinal scores - You: {user_score}, Computer: {computer_score}")
if user_score > computer_score:
    print("Congratulations, you are the overall winner!")
elif user_score < computer_score:
    print("Sorry, computer wins this game. Better luck next time!")
else:
    print("It's a tie game!")
