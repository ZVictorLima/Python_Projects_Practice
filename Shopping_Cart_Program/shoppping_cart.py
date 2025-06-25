# Shopping Cart Program

# This program is meant to train Lists,Sets and Tuples in Python

  

# Create a list to store the items in the cart

# List in this case is the best option because we can have duplicates and easy to manipulate

foods = []

prices = []

Total = 0

  

# Create a loop to add items to the cart

while True:

    # Ask the user for the item

    food = input("Enter the food you want to add to the cart (q to quit): ")

    if food.lower() == 'q': #in case the user uses a capital letter

        break

    else:

        price = float(input(f"Enter the price for {food}: $"))

        foods.append(food)

        prices.append(price)

        Total += price

# Print the items in the cart

print("Items in the cart:")

for i in range(len(foods)):

    print(f"{foods[i]} - ${prices[i]}")

  

print(f"Total: ${Total}")