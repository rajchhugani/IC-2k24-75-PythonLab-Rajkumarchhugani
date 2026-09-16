# ATM Simulation
# This program provides a menu-driven ATM system.


INITIAL_BALANCE = 5000
INITIAL_PIN = "1234"


def get_amount(prompt):
    """Take and validate a non-negative amount."""

    while True:
        try:
            amount = float(input(prompt))

            if amount < 0:
                print("Amount cannot be negative.")
            else:
                return amount

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def atm_menu(balance):
    """Run the ATM menu and return the updated balance."""

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"Current balance: ₹{balance:.2f}")

        elif choice == "2":
            amount = get_amount("Enter deposit amount: ")

            if amount == 0:
                print("Deposit amount must be greater than zero.")
            else:
                balance += amount
                print(f"₹{amount:.2f} deposited successfully.")
                print(f"New balance: ₹{balance:.2f}")

        elif choice == "3":
            amount = get_amount("Enter withdrawal amount: ")

            if amount == 0:
                print("Withdrawal amount must be greater than zero.")

            elif amount > balance:
                print("Transaction rejected.")
                print("Insufficient balance.")

            else:
                balance -= amount
                print(f"₹{amount:.2f} withdrawn successfully.")
                print(f"Remaining balance: ₹{balance:.2f}")

        elif choice == "4":
            old_pin = input("Enter current PIN: ")

            if old_pin == INITIAL_PIN:
                new_pin = input("Enter new 4-digit PIN: ")

                if len(new_pin) == 4 and new_pin.isdigit():
                    print("PIN changed successfully.")
                else:
                    print("PIN must contain exactly 4 digits.")
            else:
                print("Incorrect current PIN.")

        elif choice == "5":
            print("Exiting ATM...")
            return balance

        else:
            print("Invalid menu choice. Please try again.")


def main():
    """Start the ATM application."""

    balance = INITIAL_BALANCE
    pin = input("Enter your PIN: ")

    if pin != INITIAL_PIN:
        print("Incorrect PIN. Access denied.")
        return

    print("PIN accepted. Welcome!")

    atm_menu(balance)


if __name__ == "__main__":
    main()