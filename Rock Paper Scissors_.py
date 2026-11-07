import random

score = 0
pc_score = 0
turns = 0
choices = ("Rock", "Paper", "Scissors")

while turns < 10:  # Play 10 rounds
    print(f"\n--- Round {turns + 1} ---")
    choice = input(
        "What do you choose (Rock, Paper, Scissors)?: ").strip().capitalize()

    if choice not in choices:
        print("Invalid choice! Try again.")
        continue  # Skips the turn increment if they type something invalid

    pc_choice = random.choice(choices)

    print(f"You chose: {choice}")
    print(f"Computer chose: {pc_choice}")

    if choice == pc_choice:
        print("Draw")
    elif (
        (choice == "Rock" and pc_choice == "Scissors") or
        (choice == "Paper" and pc_choice == "Rock") or
        (choice == "Scissors" and pc_choice == "Paper")
    ):
        print("You Win")
        score += 1
    else:
        print("You lose")
        pc_score += 1

    turns += 1

print("\n=== Final Score ===")
print(f"You: {score} | Computer: {pc_score}")
if score < pc_score:
    print("You've lost, Better luck next time!")
elif score == pc_score:
    print("It's a Draw!")
else:
    print("Congratulations, you've won!!")
