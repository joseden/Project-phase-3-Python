# Project-phase-3-Python

# Banking System CLI : Synposis
This is a simple Command-Line Interface (CLI) program for a banking system. It allows users to perform basic banking operations such as checking balance, depositing money, and withdrawing money. This program uses one to many association sql alchemy where The program ensures that when a new deposit or withdrawal is made, the account balance is automatically updated and reflects the change in real-time.


 # Requirements

1. Python 3.x
2. SQLAlchemy
3. Faker
4. Alembic

# Installation
Clone this repository to your local machine:

bash

"git clone https://github.com/your-username/banking-system.git"

Navigate to the project directory:

bash

cd lib 

Install the required dependencies:

bash

"pip install -r requirements.txt"

# Usage

Run the main.py file to start the CLI application:

bash

"python main.py"

Follow the on-screen instructions to perform banking operations:

Enter your choice based on the menu displayed.
Provide the required information such as account ID and amount.


# MVP
1. Check balance: View the current balance of a specific account.
2. Deposit: Add money to an account.
3. Withdraw: Remove money from an account.

# Account Model:
The Account model represents bank accounts.
It has attributes such as id, name, balance, and password.
The balance attribute represents the current balance of the account.
It has a one-to-many relationship with both Deposit and Withdrawal models, which represent the transactions associated with the account.
We've defined an event listener that triggers after an account is updated. This listener updates the amounts in the Deposit and Withdrawal tables associated with the account.

# Deposit Model:
The Deposit model represents deposits made into accounts.
It has attributes such as deposit_id, account_id, amount, and timestamp.
It is associated with the Account model through a foreign key relationship.
We've defined an event listener that triggers after a deposit is inserted. This listener updates the account balance by adding the deposited amount to it.


# Withdrawal Model:
The Withdrawal model represents withdrawals made from accounts.
It has attributes such as withdrawal_id, account_id, amount, and timestamp.
It is associated with the Account model through a foreign key relationship.



You can further enhance the README with additional details such as how to extend the functionality, project structure, etc., based on your requirements.

# License
This project is licensed under the MIT License - see the LICENSE file for details.





            

    
    

            