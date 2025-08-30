from account import Account
from auth import authenticate_user
from utils import clear_screen, display_header
from transactions import handle_transaction

def main():
    """Main function that runs the ATM simulation."""
    # Initialize accounts
    accounts = {
        "123456": Account("123456", "1234", 5000.00),
        "654321": Account("654321", "4321", 3000.00)
    }

    clear_screen()
    display_header("Welcome to the Ceylon Bank ATM")

    # Authenticate user
    account = authenticate_user(accounts)
    if not account:
        print("\nToo many incorrect attempts. Your account is temporarily locked.")
        input("\nPress Enter to exit...")  # <-- Keeps console open
        return

    # Main transaction loop
    while True:
        clear_screen()
        display_header(f"Account: {account.account_number}")
        print("\nPlease select an option:")
        print("1. View Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Mini Statement")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":
            handle_transaction(account, "balance")
        elif choice == "2":
            handle_transaction(account, "deposit")
        elif choice == "3":
            handle_transaction(account, "withdraw")
        elif choice == "4":
            handle_transaction(account, "change_pin")
        elif choice == "5":
            handle_transaction(account, "mini_statement")
        elif choice == "6":
            print("Thank you for using our Ceylon Bank ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
