# Roll Dice

import random

player_score = 0
pc_score = 0

while True:
    choice = input('Roll the dice? (y/n): ').lower()
    if choice == 'y':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        pc_dice1 = random.randint(1, 6)
        pc_dice2 = random.randint(1, 6)

        player_total = dice1 + dice2
        pc_total = pc_dice1 + pc_dice2

        print(f"You rolled ({dice1}, {dice2}) - Total: {player_total}")
        print(f"Opponent rolled ({pc_dice1}, {pc_dice2}) - Total: {pc_total}")

        if player_total > pc_total:
            print("You win this round!\n")
            player_score += 1
        elif player_total < pc_total:
            print("Opponent wins this round!\n")
            pc_score += 1
        else:
            print("It's a tie!\n")

        print(f"Score -> You: {player_score} | Opponent: {pc_score}\n")

    elif choice == 'n':
        print(
            f"\nThanks for playing! Final Score -> You: {player_score} | Opponent: {pc_score}")
        break
    else:
        print('Invalid choice!\n')
