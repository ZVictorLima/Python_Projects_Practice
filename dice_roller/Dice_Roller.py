import random   # Importing the random module

# ACII art for the dice
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

# Function to roll the dice
def roll_dice():
    return random.randint(1,6)

dice = []   # List to store the dice rolls
total = 0   # Variable to store the total of the dice rolls
num_of_dice = int(input("Enter the number of dice you want to roll: "))   # Input from the user for the number of dice to roll

# Loop to roll the dice
for die in range(num_of_dice):
    dice.append(roll_dice())
    total += dice[die]
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="  ")
    print()

print("The dice rolls are: ", dice)
print("The total is: ", total)
