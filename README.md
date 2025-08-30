## ATM Simulation by sanuth mallawaarachchi

A Python based ATM simulation that allows users to perform basic banking operations.

## How to Run

1. Ensure you have Python 3.6 or higher installed
2. Download all the Python files into the same directory
3. Open a terminal/command prompt in that directory
4. Run the program with: `main.py`

## Default Accounts

For testing purposes, the following accounts are pre-loaded:

- Account: 123456, PIN: 1234, Balance: $5000.00
- Account: 654321, PIN: 4321, Balance: $3000.00

## File Structure

1.	`account.py` # Account class and related methods
2.	`auth.py` # Authentication logic
3.	`utils.py` # Helper functions (clear screen, header, valid amount)
4.	`transactions.py` # Transaction handling
5.	`main.py` # Main program entry point

## Features

- Account authentication with PIN verification
- Balance inquiry
- Cash deposits
- Cash withdrawals with balance checks
- PIN change functionality
- Mini statement showing last 5 transactions
- Account locking after 3 failed login attempts
- Input validation for all operations
