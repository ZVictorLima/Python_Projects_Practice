'''

 This is a project that simulates a banking system

    The system will have the following features:

                                                1. Show balance

                                                2. Deposit

                                                3. Withdraw

 The purpose is to get a better understanding of functions

'''

'''

Function to show balance

    Input: None

    Output: Balance

'''

def show_balance(balance):

    print(f"Your balance is: ${balance}")

  

# Function to deposit

def deposit(balance):

    amount_to_deposit = float(input("How much would you like to deposit? "))

    if amount_to_deposit <= 0:

        return "Invalid Amount"

    return amount_to_deposit

  

'''

Function to withdraw

    Input: Amount to withdraw

    Do : Check if the amount is available to withdraw, if it is, withdraw the amount

    Output: text saying if the withdraw was successful or not

'''

def withdraw(balance):

    amount_to_withdraw = float(input("How much would you like to withdraw? "))

    if balance >= amount_to_withdraw:

        return amount_to_withdraw

    else:

        print("Insufficient funds")

        return 0

def main():  

    balance = 0  # balance is a global variable

    is_running = True

  

    while is_running:

        user_choice = input("What would you like to do? (1.show balance, 2.deposit, 3.withdraw, 4.quit): ")

        match user_choice:

            case "1":

                show_balance(balance)

  

            case "2":

                balance += deposit(balance)

  

            case "3":

                balance -= withdraw(balance)

            case "4":

                is_running = False

  
  

if __name__ == "__main__":

    main()