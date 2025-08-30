from utils import get_valid_amount

def handle_transaction(account, transaction_type):
    """Handle different types of transactions."""
    if transaction_type == "balance":
        print(f"\nYour current balance is: Rs.{account.get_balance():.2f}")

    elif transaction_type == "deposit":
        amount = get_valid_amount("Enter deposit amount: Rs.")
        if amount is not None:
            success, message = account.deposit(amount)
            print(f"\n{message}")

    elif transaction_type == "withdraw":
        amount = get_valid_amount("Enter withdrawal amount: Rs.")
        if amount is not None:
            success, message = account.withdraw(amount)
            print(f"\n{message}")

    elif transaction_type == "change_pin":
        new_pin = input("Enter new 4-digit PIN: ")
        confirm_pin = input("Confirm new PIN: ")
        if new_pin != confirm_pin:
            print("PINs do not match.")
        else:
            success, message = account.change_pin(new_pin)
            print(f"\n{message}")

    elif transaction_type == "mini_statement":
        print("\n" + account.get_mini_statement())
