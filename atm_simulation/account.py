from datetime import datetime

class Account:
    """Represents a bank account with transaction capabilities."""

    def __init__(self, account_number, pin, balance=0.0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transactions = []
        self.failed_attempts = 0
        self.locked = False

    def check_pin(self, pin):
        return self.pin == pin

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            return False, "Amount must be positive."
        self.balance += amount
        self._add_transaction("Deposit", amount)
        return True, f"Successfully deposited ${amount:.2f}"

    def withdraw(self, amount):
        if amount <= 0:
            return False, "Amount must be positive."
        if amount > self.balance:
            return False, "Insufficient funds."
        self.balance -= amount
        self._add_transaction("Withdrawal", amount)
        return True, f"Successfully withdrew ${amount:.2f}"

    def change_pin(self, new_pin):
        if len(new_pin) != 4 or not new_pin.isdigit():
            return False, "PIN must be a 4-digit number."
        self.pin = new_pin
        self._add_transaction("PIN Change", 0)
        return True, "PIN changed successfully."

    def get_mini_statement(self):
        if not self.transactions:
            return "No transactions yet."
        statement = "Date\t\tType\t\tAmount\tBalance\n"
        statement += "-" * 50 + "\n"
        for transaction in self.transactions[-5:]:
            date = transaction['date'].strftime("%Y-%m-%d %H:%M")
            t_type = transaction['type'].ljust(10)
            amount = f"${transaction['amount']:.2f}".ljust(10)
            balance = f"${transaction['balance']:.2f}"
            statement += f"{date}\t{t_type}\t{amount}\t{balance}\n"
        return statement

    def _add_transaction(self, transaction_type, amount):
        transaction = {
            'date': datetime.now(),
            'type': transaction_type,
            'amount': amount,
            'balance': self.balance
        }
        self.transactions.append(transaction)
        if len(self.transactions) > 5:
            self.transactions = self.transactions[-5:]

    def increment_failed_attempts(self):
        self.failed_attempts += 1
        if self.failed_attempts >= 3:
            self.locked = True

    def reset_failed_attempts(self):
        self.failed_attempts = 0
