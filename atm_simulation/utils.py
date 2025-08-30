import os

def get_valid_amount(prompt):
    """Get a valid monetary amount from the user."""
    try:
        amount = float(input(prompt))
        if amount <= 0:
            print("Amount must be positive.")
            return None
        return amount
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return None

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header(title):
    print("=" * 50)
    print(f"{title:^50}")
    print("=" * 50)
