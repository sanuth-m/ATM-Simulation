def authenticate_user(accounts):
    """Authenticate a user by account number and PIN."""
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        account_number = input("Enter your account number: ")
        pin = input("Enter your PIN: ")

        if not account_number.isdigit() or not pin.isdigit():
            print("Account number and PIN must be numeric.")
            attempts += 1
            continue

        if account_number not in accounts:
            print("Account not found.")
            attempts += 1
            continue

        account = accounts[account_number]

        if account.locked:
            print("**")
            return None

        if account.check_pin(pin):
            account.reset_failed_attempts()
            return account
        else:
            account.increment_failed_attempts()
            attempts += 1
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"Incorrect PIN. {remaining} attempt(s) remaining.")
    return None
