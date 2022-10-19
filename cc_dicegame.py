import random

high_score = 0


def dice_game():
    while True:
        global high_score
        print("Current High Score:", high_score)
        print("1) Roll Dice")
        print("2) Leave Game")
        choice = input("Enter your choice:")
        if choice == 2:
            print("Well, goodbye then!")
            break

        else:
            roll_1 = random.randint(1, 6)
            roll_2 = random.randint(1, 6)

            total = roll_1 + roll_2

            print("You rolled a", (roll_1))
            print("You rolled a", (roll_2))
            print("You have rolled a total of:", (total))

            if total > high_score:
                print("New high score!")

                high_score = total
            continue


dice_game()
