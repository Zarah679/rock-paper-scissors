import random

#prompting user for input
user = input("What is your choice? ('r' for rock, 'p' for paper, 's' for scissors): ")
possible_choices = ["r", "p", "s"]
computer  = random.choice(possible_choices)

print(f"\nYou chose {user}, computer chose {computer}.\n")

#apply control flow to determine a winner
#rock > scissors, scissors > paper, paper > rock

if user == computer:
    print(f"Both players selected {user}. It's a tie!")
elif user == "r":
    if computer == "s":
        print("Rock destroys scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user == "p":
    if computer == "r":
        print("Paper covers rock! You win!")
    else:
        print("Scissors shreds paper! You lose.")
elif user == "s":
    if computer == "p":
        print("Scissors shreds paper! You win!")
    else:
        print("Rock destroys scissors! You lose.")