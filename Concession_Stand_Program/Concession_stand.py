# In this program, we will simulate a concession stand at a movie theater.

# By using Dictionary

  

menu = {"popcorn":5.00,

        "soda":2.00,

        "candy":3.00,

        "hotdog":4.00,

        "water":1.00}

  

# a user is going to select specific keys from the menu and we can calculate the total cost of the items selected

  

cart = []

  

total = 0

  

print("_+_+_+_+_MENU_+_+_+_+_+_")

for key,value in menu.items():

    print(f"{key:10} - ${value:.2f}")

print("------------------------ ")

  

while True:

    food = input("Enter the item you want to order: ").lower()

    if food == "quit":

        break

    if food in menu:

        cart.append(food)

        total += menu[food]

    else:

        print(f"Item {food} is not available")

  

# Lets print what the user selected

print("You have selected: ")

for item in cart:

    print(f"{item:10} - ${menu[item]:.2f}")

print (f"total: ${total:.2f}")