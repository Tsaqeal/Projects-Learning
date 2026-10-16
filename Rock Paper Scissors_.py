import random

score = 0
pc_score = 0
turns = 0
choices = ("Rock", "Paper", "Scissors")

while turns < 10:  # Play 10 rounds
    print(f"\n--- Round {turns + 1} ---")
    choice = input("What u choose : Rock, Paper, Scissors?: ")
    pc_choice = random.choice(choices)

    print(f"You chose: {choice}")
    print(f"Computer chose: {pc_choice}")

    if choice == "Rock":
        if pc_choice == "Scissors":
            print("You Win")
            score += 1
        elif pc_choice == "Rock":
            print("Draw")
        else:
            print("You lose")
            pc_score += 1
    elif choice == "Paper":
        if pc_choice == "Rock":
            print("You Win")
            score += 1
        elif pc_choice == "Paper":
            print("Draw")
        else:
            print("You lose")
            pc_score += 1
    elif choice == "Scissors":
        if pc_choice == "Paper":
            print("You Win")
            score += 1
        elif pc_choice == "Scissors":
            print("Draw")
        else:
            print("You lose")
            pc_score += 1
    else:
        print("Invalid choice! Try again.")
        continue  # Skips the turn increment if they type something invalid

    turns += 1

print("\n=== Final Score ===")
print(f"You: {score} | Computer: {pc_score}")
